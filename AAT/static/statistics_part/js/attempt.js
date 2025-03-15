function getAttempts(){
    //fetch the resource, which is a class that inherits resource,which links to the database
    //js file->routes.py->FA.py
    fetch("/api/FormativeAttempt/")//url in routes.py
    .then(responseObject=>responseObject.json())
    .then(res=>setAttemptsTable(res));
}
function setAttemptsTable(res){//res is an array of js objects,each object is a row
    console.log("response result"+res);
    console.log("response result one row"+res[0]);
    let table_body=document.getElementById("attempt_body");
    const DEFAULT_ASSESSMENT=1;//decide to show result of assessment 1 by default

    //show attempt for each assessment
    const COLS_NAME=["student_id","student_name","assessment_name","attempts"];
    for (let i=0;i<res.length;i++){
        if (res[i][assessment_id]==DEFAULT_ASSESSMENT){
            currRow=document.createElement("tr");
            for (let j=0;j<COLS_NAME.length;j++){
                currCol=document.createElement("td");
                currCol.textContent=res[i][COLS_NAME[j]];
                currRow.appendChild(currCol);
            }
        }
        

        
        table_body.appendChild(currRow);
        
    }
}
window.onload=getAttempts();