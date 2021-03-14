const root = document.querySelector(".main-container")
const classContainer = document.querySelector(".class-container")
console.log(root)
console.log(classContainer)
root.appendChild(classContainer)
var grade;
var board;

function getBoard(val){
	grade = val;
	console.log(grade);
    root.removeChild(classContainer)
    document.querySelector(".board-container").style.display = "block";
    root.appendChild(document.querySelector(".board-container"))

}

function getCourse(val){
	board = val;
	console.log(board);
    root.removeChild(document.querySelector(".board-container"))
    document.querySelector(".course-container").style.display = "block"
    root.appendChild(document.querySelector(".course-container"))
}
var course;
function genMentor(val){
    course = val
    console.log(course)
    root.removeChild(document.querySelector(".course-container"))
    document.querySelector(".mentor-container").style.display = "block";
    root.appendChild(document.querySelector(".mentor-container"))

}

function genBill(mentorship){
	$.ajax(
	{
		type:"POST",
		datatype:"text",
		//url:"{% url 'additional_details'%}",
		url:"/additional_details/",
		data:{
				Grade:grade,
				Board:board,
				Course:course,
				Mentorship:mentorship,
		},

	
	success:function(data){
		    root.removeChild(document.querySelector(".mentor-container"))
		    if(course == 'Regular' && mentorship == '1v1'){
		        document.querySelector(".r1-container").style.display = "block";
		        root.appendChild(document.querySelector(".r1-container"))
		    }
		    else if(course == 'Regular' && mentorship == '1v5'){
		        document.querySelector(".r5-container").style.display = "block";
		        root.appendChild(document.querySelector(".r5-container"))
		    }
		    else if(course == 'Crash' && mentorship == '1v1'){
		        document.querySelector(".c1-container").style.display = "block";
		        root.appendChild(document.querySelector(".c1-container"))
		    }
		    else{
		        document.querySelector(".c5-container").style.display = "block";
		        root.appendChild(document.querySelector(".c5-container"))
		    }
		},

	})



}