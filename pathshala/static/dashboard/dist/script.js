function genCourseContent(val, year){
  year = year + "th"
  if(year === "8th"){
    if(val === 0){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".physics-container-8")
      details.style.display = "block"
    }
    if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".chemistry-container-8")
      details.style.display = "block"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".maths-container-8")
      details.style.display = "block"
    }
    if(val === 3){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".biology-container-8")
      details.style.display = "block"
    }
  } else if ( year === "9th"){
    if(val === 0){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".physics-container-9")
      details.style.display = "block"
    }
    if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".chemistry-container-9")
      details.style.display = "block"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".maths-container-9")
      details.style.display = "block"
    }
    if(val === 3){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".biology-container-9")
      details.style.display = "block"
    }
  } else if ( year === "10th"){
    if(val === 0){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".physics-container-10")
      details.style.display = "block"
    }
    if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".chemistry-container-10")
      details.style.display = "block"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".maths-container-10")
      details.style.display = "block"
    }
    if(val === 3){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".biology-container-10")
      details.style.display = "block"
    }
  }else if ( year === "11th"){
    if(val === 0){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".physics-container-11")
      details.style.display = "block"
    }
    if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".chemistry-container-11")
      details.style.display = "block"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".maths-container-11")
      details.style.display = "block"
    }
  }else if ( year === "12th"){
    if(val === 0){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".physics-container-12")
      details.style.display = "block"
    }
    if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".chemistry-container-12")
      details.style.display = "block"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "none"
      details = document.querySelector(".maths-container-12")
      details.style.display = "block"
    }
  }
}

function genSubjects(val, year){
  if (year === 8){
    if(val==0){
      details = document.querySelector(".physics-container-8")
      details.style.display = "none"
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
    }
    else if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".chemistry-container-8")
      details.style.display = "none"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".maths-container-8")
      details.style.display = "none"
    }
    if(val === 3){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".biology-container-8")
      details.style.display = "none"
    }
  } else if (year === 9){
    if(val==0){
      details = document.querySelector(".physics-container-9")
      details.style.display = "none"
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
    }
    else if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".chemistry-container-9")
      details.style.display = "none"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".maths-container-9")
      details.style.display = "none"
    }
    if(val === 3){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".biology-container-9")
      details.style.display = "none"
    }
  } else if( year === 10) {
    if(val==0){
      details = document.querySelector(".physics-container-10")
      details.style.display = "none"
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
    }
    else if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".chemistry-container-10")
      details.style.display = "none"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".maths-container-10")
      details.style.display = "none"
    }
    if(val === 3){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".biology-container-10")
      details.style.display = "none"
    }
  }else if(year === 11) {
    if(val==0){
      details = document.querySelector(".physics-container-11")
      details.style.display = "none"
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
    }
    else if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".chemistry-container-11")
      details.style.display = "none"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".maths-container-11")
      details.style.display = "none"
    }
  }
  else if(year === 12){
    if(val==0){
      details = document.querySelector(".physics-container-12")
      details.style.display = "none"
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
    }
    else if(val === 1){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".chemistry-container-12")
      details.style.display = "none"
    }
    if(val === 2){
      subject = document.querySelector(".subjects-container")
      subject.style.display = "block"
      details = document.querySelector(".maths-container-12")
      details.style.display = "none"
    }
  }
}