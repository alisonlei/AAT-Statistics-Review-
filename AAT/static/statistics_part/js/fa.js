
// function simulateSubmission(){
//     let btn=document.getElementById("simulate submission");
//     console.log("test")
//     btn.addEventListener("click",function(){
//         fetch("/handleFsSubmission", {
    
//             // Adding method type
//             method: "POST",
            
//             // Adding body or contents to send
//             body: JSON.stringify({
//                 student_id: 1,
//                 assessment_id: 1,
                
//             }),
            
//             // Adding headers to the request
//             headers: {
//                 "Content-type": "application/json; charset=UTF-8"
//             }
//         })
        
//         // Converting to JSON
//         .then(response => response.json())
        
//         // Displaying results to console
//         .then(json => console.log(json));
//     })
// }
// simulateSubmission();
function setAttemptCDN(){
    console.log("running setCDN for Attempt table");
    
    let jq_code=document.createElement("script");
    

    let body=document.body;
   
    const initializeTable=`    $(document).ready( function () {
        $('#attempt_table').DataTable();
       
    } );
    `
    jq_code.textContent=initializeTable;
    body.appendChild(jq_code);

}

// take a set as input
// function setAssessmentList(assessment_lt){
//     let option;
//     //elements in ordered_lt are numbers not string
//     let ordered_lt=[...assessment_lt].sort((a, b) => a - b);
//     console.log(typeof ordered_lt[0]);
//     let menu=document.getElementById("assessment_list");
//     for (let i=0;i<ordered_lt.length;i++){
//         option=document.createElement("li");
//         option.onclick=getOtherFAAttempts(ordered_lt[i]);
//         option.textContent=ordered_lt[i];
//         menu.appendChild(option);
//     }

// }
function renewAttemptsTable(data){
    let table=document.getElementById("attempt_body");
    let new_rows_count=data.length;
    
    

    let rows=table.children;
    let original_row_count=rows.length;
    let excess_children=new_rows_count-original_row_count;
    const COLS_NAME=["student_id","student_name","assessment_name","attempts"];
    let title=document.getElementById("assessment_name");
    title.textContent=data[0]["assessment_name"];
    if (excess_children<0){//new lt < old lt
        for (let i=1;i<=new_rows_count;i++){//erase and write new content 
            for(let j=0;j<COLS_NAME.length;j++){
                rows[i-1].children[j].textContent=data[i-1][COLS_NAME[j]];
            }
        }
        for (let i=new_rows_count;i<original_row_count;i++){//remove extra rows
            rows.removeChild(rows[i])
        }
    }else{
        for (let i=0;i<original_row_count;i++){
            for(let j=0;j<COLS_NAME.length;j++){
                rows[i].children[j].textContent=data[i][COLS_NAME[j]];
            }
        }
        let excess_i=original_row_count;
        let new_row;
        if (excess_children>0){
            for (let i=0;i<excess_children;i++){
                new_row=document.createElement("tr");
                for(let j=0;j<COLS_NAME.length;j++){//create col for the curr excess row
                    new_cell=document.createElement("td");
                    new_cell.textContent=data[excess_i][j];
                    new_row.appendChild(new_cell);
                }
                table.append(new_row);
                excess_i++;//go to the next excess row
            }
        }
    }

}
function getOtherFAAttempts(assessment_id){
    return function(){
        let get_content="/api/FormativeAttempt/"+assessment_id;
        fetch(get_content)
        
        .then((response) =>response.json())
        
        .then((data) => renewAttemptsTable(data));
    
    };   
}
function setParametersByFAName(){
    let options=document.getElementsByClassName("parameter");
    for (let i=1;i<=options.length;i++){
        options[i-1].onclick=getOtherFAAttempts(i);
    }
}
function setAttemptsTable(res){//res is an array of js objects,each object is a row
    console.log("running SET attempttable");
    
    let title=document.getElementById("assessment_name");
    title.textContent=res[0]["assessment_name"];
    setParametersByFAName();
    let table_body=document.getElementById("attempt_body");

    //show attempt for each assessment
    const COLS_NAME=["student_id","student_name","assessment_name","attempts"];
    let assessment_lt=new Set();
    for (let i=0;i<res.length;i++){
      
        
        currRow=document.createElement("tr");
        for (let j=0;j<COLS_NAME.length;j++){
            currCol=document.createElement("td");
            currCol.textContent=res[i][COLS_NAME[j]];
            currRow.appendChild(currCol);
        }

        table_body.appendChild(currRow);
  
    }
    
    setAttemptCDN();
}
function getAttempts(){//default is get the first assessment
    console.log("running get attempt");
    //fetch the resource, which is a class that inherits resource,which links to the database
    //js file->routes.py->FA.py
    fetch("/api/FormativeAttempt/1")//url in routes.py
    .then(responseObject=>responseObject.json())
    .then(res=>setAttemptsTable(res));
    
}
function setResponseCDN(){
    console.log("running setCDN");
    
    let jq_code=document.createElement("script");
    

    let body=document.body;
   
    const initializeTable=`    $(document).ready( function () {
        $('#response_table').DataTable();
       
    } );
    `
    jq_code.textContent=initializeTable;
    body.appendChild(jq_code);

}
function initialize_topic_parameters(){
    let topic_parameters=document.getElementsByClassName("topic");
    
    for (let p of topic_parameters){
        p.addEventListener("click",function(){
            let table_body=document.getElementById("response_body");
            let table_rows=table_body.children;
            let response_rows_count=table_rows.length;
            for (let i=0;i<response_rows_count;i++){
                if (table_rows[i].children[2].textContent!=p.textContent){
                    table_rows[i].style.display='none';
                }else{
                    table_rows[i].style.display='table-row';
                }
            }
        })
    }
    let reset=document.getElementsByClassName("all_topics")[0];
    reset.addEventListener("click",function(){
        let table_body=document.getElementById("response_body");
        let table_rows=table_body.children;
        let response_rows_count=table_rows.length;
        for (let i=0;i<response_rows_count;i++){
            table_rows[i].style.display='table-row';
       
    }
    })
   
}
function setResponsesTable(res){//res is an array of js objects,each object is a row
    console.log("running setresponsetable");
    let table_body=document.getElementById("response_body");
    
    //add event listener to topic parameters

    initialize_topic_parameters();
    
    

    //create rows of question responses
    const COLS_NAME=["exe_id","exe_content","topic","incorrect_response","correct_response"];
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
function getResponsesandAttempts(){
    //fetch the resource, which is a class that inherits resource,which links to the database
    //js file->routes.py->FA.py
    console.log("running get resposne and attempt");
    fetch("/api/Formative/")//url in routes.py
    .then(responseObject=>responseObject.json())
    .then(res=>setResponsesTable(res));
    getAttempts();
    
}
window.onload=getResponsesandAttempts();
