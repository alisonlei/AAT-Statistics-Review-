//import * as indiv_res from './indiv_sa.js';


function create_graph(data){
    // d3.select("#sum_res")
    // .style("margin",auto);
    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 30, bottom: 70, left: 50},
    width = 1000 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;
    
    // append the svg object to the body of the page
    var svg = d3.select("#sum_res")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .style("display","block")
    .style("margin","auto")
    .append("g")
    .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");
     
    
  
    //format the data from sqlite/python flask for use in d3
    let years=[];
    let res_by_years=[];
    for (const [year, scores] of Object.entries(data)){
      res_by_years.push({year:year,scores:scores.sort((a, b) => a - b)});//organize sa result data from a dictionary into  a list of js object literals
      //each object is sa result in a year , the purpose is for populate the graph with the data with d3.
      years.push(year);//this is for creating the x-axis domain
    }
    //create an array of objects which are data object. The data object is here is a box in box-plot.
    //the format of a data object in d3 is always {key:attribute,values:list of values}.
    //e.g. {name:"alison",contacts:[phone,email]},it is essentailly a table row.
    //different from python dict, which maps "alison" directly to [phone,email],i.e.{"alison":[phone,email]}
    let sumstat=[];
    for (let resObj of res_by_years){
      q1 = d3.quantile(resObj.scores,.25);
      median = d3.quantile(resObj.scores,.5);
      q3 = d3.quantile(resObj.scores,.75);
      interQuantileRange = q3 - q1;
      min = q1 - 1.5 * interQuantileRange;
      max = q3 + 1.5 * interQuantileRange;
      sumstat.push({key:resObj.year,values:{
        q1:q1,median:median,q3:q3,interQuantileRange:interQuantileRange,min:min,max:max
      }})
    }
    
    //set up legend

    var keys=[2022,2023,2024];
    var colors=["red","green","grey"];
    var color = d3.scaleOrdinal()
    .domain(years)
    .range(colors);
    var size = 20

    
    svg.selectAll("mydots")
      .data(keys)
      .enter()
      .append("rect")
        .attr("x", 850)
        .attr("y", function(d,i){ return 100 + i*(size+5)}) // 100 is where the first dot appears. 25 is the distance between dots
        .attr("width", size)
        .attr("height", size)
        .style("fill", function(d){ return color(d)})
    
    // Add one dot in the legend for each name.
    svg.selectAll("mylabels")
      .data(keys)
      .enter()
      .append("text")
        .attr("x", 850 + size*1.2)
        .attr("y", function(d,i){ return 100 + i*(size+5) + (size/2)}) // 100 is where the first dot appears. 25 is the distance between dots
        .style("fill", function(d){ return color(d)})
        .text(function(d){ return d})
        .attr("text-anchor", "left")
        .style("alignment-baseline", "middle")
// Show the X scale
var x = d3.scaleBand()
  .range([ 0, width ])
  .domain(years)
  .paddingInner(1)
  .paddingOuter(.5)
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x))

// Show the Y scale
var y = d3.scaleLinear()
  .domain([-100,200])
  .range([height, 0])
svg.append("g").call(d3.axisLeft(y))

// Show the main vertical line
svg
  .selectAll("vertLines")
  .data(sumstat)
  .enter()
  .append("line")
    .attr("x1", function(d){return(x(d.key))})
    .attr("x2", function(d){return(x(d.key))})
    .attr("y1", function(d){return(y(d.values.min))})
    .attr("y2", function(d){return(y(d.values.max))})
    .attr("stroke", "black")
    .style("width", 40)
    



// rectangle for the main box
var boxWidth = 50
svg
  .selectAll("boxes")
  .data(sumstat)
  .enter()
  .append("rect")
      .attr("x", function(d){return(x(d.key)-boxWidth/2)})
      .attr("y", function(d){return(y(d.values.q3))})
      .attr("height", function(d){return(y(d.values.q1)-y(d.values.q3))})
      .attr("width", boxWidth )
      .attr("stroke", "black")
      // .style("fill", "#69b3a2")
      .on("mouseover",function(d){
        tooltip
            .style("visibility", "visible")
            
      })
      .on("mousemove",function(d){
        tooltip
        .style("left", (d3.mouse(this)[0]+300) + "px")
        .style("top", (d3.mouse(this)[1]+70) + "px")
        .style("z-index",1000)
        .html("<p>min:"+d.values.min+"<br>"+
               "lower quartile:"+d.values.q1+"<br>"+
                "median:"+d.values.median+"<br>"+
                "upper quartile:"+d.values.q3+"<br>"+
                "max:"+d.values.max+"</p>")
        .style("line-height","1.3");
              
      })
      .on("mouseout",function(d){
        tooltip
        .style("visibility", "hidden");
      });

  //set all boxes color to the corresponding color using d3.,the feature of binding data to elements.
let boxes=d3.selectAll("rect");
boxes.each(function(d,i){
  d3.select(this).style("fill",colors[i%colors.length])
})
// Show the median
svg
  .selectAll("medianLines")
  .data(sumstat)
  .enter()
  .append("line")
    .attr("x1", function(d){return(x(d.key)-boxWidth/2) })
    .attr("x2", function(d){return(x(d.key)+boxWidth/2) })
    .attr("y1", function(d){return(y(d.values.median))})
    .attr("y2", function(d){return(y(d.values.median))})
    .attr("stroke", "black")
    .style("width", 80)
//add y-axis label
    svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x",0 - (height / 2))
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .text("Score"); 
//add x-axis label
svg.append("text")
.attr("y", height+25 )
.attr("x", width/2)
.attr("dy", "1em")
.style("text-anchor", "middle")
.text("Year of Intake"); 
//tooltip for showing the values of the boxes
   var tooltip=d3.select("#sum_res")
   .append("div").attr("class","tooltip")
 
    .style("position","absolute")
    .style("visibility", "hidden")
    .style("background-color", "white")
    .style("border", "solid")
    .style("border-width", "1px")
    .style("border-radius", "5px")
    .style("padding", "10px")
   


 }
  
 


function get_sum_data(assessment_id,cohort){
  //0 represents cohort, 1 indiv
    console.log("this is from js get_sum_data");
    let url="/api/Attainment/" + assessment_id+"/"+cohort;
    fetch(url)
    .then(response=>response.json())
    .then(data=>create_graph(data));   
  
// function pass_data_to_graph(data){
//     return data
}


window.onload=function(){
  get_sum_data(1,1);
  
}
