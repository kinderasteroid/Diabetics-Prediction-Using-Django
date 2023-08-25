function checkk(){
    if(document.getElementById("Pregnency")||document.getElementById("dpf").value==""||document.getElementById("glucose").value==""||document.getElementById("insulin").value==""||document.getElementById("bloodpreasure").value==""||document.getElementById("bmi").value==""||document.getElementById("age").value==""||document.getElementById("skinthick").value=="")
    {
      
    document.getElementById("myform").addEventListener("submit", function(event) {
event.preventDefault(); // Prevent the form from submitting
    alert("Please Enter All values correctly ")
// Additional code you want to execute when the form is not submitted
});


    }
}