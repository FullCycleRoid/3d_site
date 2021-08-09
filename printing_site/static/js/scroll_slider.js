let body = document.body,
    textItem = document.querySelector(".process__block__text");

let scrollLock = "height: 876px; overflow: hidden;"
let scrollUnlock = ""

let processBlock =  document.querySelector(".process__block"),
    processImg = processBlock.children[0].children[0];

let imgArray = [
    "/static/images/process/process1.jpg",
    "/static/images/process/process2.jpg",
    "/static/images/process/process3.jpg",
    "/static/images/process/process4.jpg",
];

let positions = [

]

let paragraphs = [
    "Детали печатаются с использованием технологии FDM / FFF из филамента состоящего на 90% из металла и 10% полимера.",
    "Отпечатанная деталь находится в «зеленом состоянии» и должна пройти процесс удаления полимерного связующего.",
    "После удаления связки деталь становится относительно пористой и требует процесса спекания для получения твердой и плотной детали.",
    " Когда спеченная деталь готова к использованию, возможна дополнительная постобработка для создания желаемого" +
    " качества поверхности с помощью полировки, фрезерования, термообработки и нанесения покрытия.\n"
]

let titles = [
    "1/4 ПЕЧАТЬ",
    "2/4 ДЕБИНДИНГ",
    "3/4 СПЕКАНИЕ",
    "4/4 МЕТАЛЛ",
]


let counter = 0
setImage(counter)

let onScrollHandler = function(e) {
    if (window.pageYOffset > 400 && window.pageYOffset < 1700) {
        counter = setCounter(e.deltaY, counter)
        // body.style.cssText = scrollLock;
        setImage(counter)
        changeTitleActiveStatus(counter)
        changeParagraphActiveStatus(counter)
    if (counter === 4 || counter === 0) {
            body.style.cssText = scrollUnlock;
    }
    }
}

function changeTitleActiveStatus(counter) {
    if (counter <= 0) {
        textItem.children[0].style.cssText = "color: #FF4140;"
        textItem.children[2].style.cssText = "color: #24242a;"
        textItem.children[4].style.cssText = "color: #24242a;"
        textItem.children[6].style.cssText = "color: #24242a;"
    } else if (counter === 1) {
        textItem.children[0].style.cssText = "color: #24242a;"
        textItem.children[2].style.cssText = "color: #FF4140;"
        textItem.children[4].style.cssText = "color: #24242a;"
        textItem.children[6].style.cssText = "color: #24242a;"
    } else if (counter === 2) {
        textItem.children[0].style.cssText = "color: #24242a;"
        textItem.children[2].style.cssText = "color: #24242a;"
        textItem.children[4].style.cssText = "color: #FF4140;"
        textItem.children[6].style.cssText = "color: #24242a;"
    } else if (counter >= 3) {
        textItem.children[0].style.cssText = "color: #24242a;"
        textItem.children[2].style.cssText = "color: #24242a;"
        textItem.children[4].style.cssText = "color: #24242a;"
        textItem.children[6].style.cssText = "color: #FF4140"
    }
}

function changeParagraphActiveStatus(counter) {
    if (counter <= 0) {
        textItem.children[1].style.cssText = "display: block"
        textItem.children[3].style.cssText = "display: none"
        textItem.children[5].style.cssText = "display: none"
        textItem.children[7].style.cssText = "display: none"
    } else if (counter === 1) {
        textItem.children[1].style.cssText = "display: none"
        textItem.children[3].style.cssText = "display: block"
        textItem.children[5].style.cssText = "display: none"
        textItem.children[7].style.cssText = "display: none"
    } else if (counter === 2) {
        textItem.children[1].style.cssText = "display: none"
        textItem.children[3].style.cssText = "display: none"
        textItem.children[5].style.cssText = "display: block"
        textItem.children[7].style.cssText = "display: none"
    } else if (counter >= 3) {
        textItem.children[1].style.cssText = "display: none"
        textItem.children[3].style.cssText = "display: none"
        textItem.children[5].style.cssText = "display: none"
        textItem.children[7].style.cssText = "display: block"
    }
}

function setCounter(deltaY, counter) {
    if (deltaY > 0 && counter < 4) {
        counter +=1
        console.log(counter)
        return counter
    } else if (deltaY < 0 && counter > 0) {
        counter -= 1
        console.log(counter)
        return counter
    } else {
        console.log(counter)
        return counter
    }
}

function setImage(counter) {
    if (counter <= 0) {
        processImg.src = imgArray[0]
    } else if (counter >= 3) {
        processImg.src = imgArray[3]
    } else {
        processImg.src = imgArray[counter]
    }
}

document.addEventListener ("wheel", onScrollHandler);