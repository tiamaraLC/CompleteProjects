/**
 * 
 */
 
 

  // the functon checks if the users answer is correct or not
  function displayAnswer1() {
    
    if (document.getElementById('optionA').checked) {
      document.getElementById('A').style.border = '3px solid red'
      document.getElementById('resultA').style.color = 'red'
      document.getElementById('resultA').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }  
    if (document.getElementById('optionB').checked) {
      document.getElementById('B').style.border = '3px solid limegreen'
      document.getElementById('resultB').style.color = 'limegreen'
      document.getElementById('resultB').innerHTML = 'Correct!'
      showCorrectAnswer1()
    }
    if (document.getElementById('optionC').checked) {
      document.getElementById('C').style.border = '3px solid red'
      document.getElementById('resultC').style.color = 'red'
      document.getElementById('resultC').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
    if (document.getElementById('optionD').checked) {
      document.getElementById('D').style.border = '3px solid red'
      document.getElementById('resultD').style.color = 'red'
      document.getElementById('resultD').innerHTML = 'Incorrect!'
      showCorrectAnswer1()
    }
  }
  
  
  function showDiv() {
   document.getElementById('answText').style.display = "block";
}
  
  // the functon displays the link to the correct answer
  function showCorrectAnswer1() {
    showDiv()
  }

