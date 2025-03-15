function setResponseCDN(){
    console.log("running setCDN");
    
    let jq_code=document.createElement("script");
    

    let body=document.body;
   
    const initializeTable=`    $(document).ready( function () {
        $('#indiv_sum').DataTable();
       
    } );
    `
    jq_code.textContent=initializeTable;
    body.appendChild(jq_code);

}

 function setIndivSaTable(res){//res is an array of js objects,each object is a row
    console.log("running setIndivSatable");
    let table_body=document.getElementById("indiv_sum_body");
    

    //create rows of indiv results
    const COLS_NAME=["student_id","intake_year","sa1","sa2"];
    for (let i=0;i<res.length;i++){
        currRow=document.createElement("tr");
        for (let j=0;j<COLS_NAME.length;j++){
            currCol=document.createElement("td");
            currCol.textContent=res[i][COLS_NAME[j]];
            currRow.appendChild(currCol);
        }
       
        currRow.appendChild(currCol);

        
        table_body.appendChild(currRow);
        
    }

    setResponseCDN();
}
function getIndivSa(){
    //fetch the resource, which is a class that inherits resource,which links to the database
    //js file->routes.py->FA.py
    console.log("running get indiv summative assessment results: ");
    fetch("/api/Attainment/1/0")//url in routes.py
    .then(response=>{
        if (! response){
            throw new Error("resposne is null or undefined");
        }
        
    return response.json();
})
     
    .then(res=>setIndivSaTable(res))
    .catch(error=>{
        console.log("fetch error"+error)});
   
}
getIndivSa();