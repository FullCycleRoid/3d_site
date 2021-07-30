let process_img = document.querySelector(".process__block__img"),
    process = document.querySelector(".process"),
    process_scrollTop_position = process_img.scrollTop,
    body = document.body;

let processBlock =  document.querySelector(".process__block"),
    processImg = processBlock.children[0],
    process__line = processBlock.children[1],
    textItemTitle = processBlock.children[2].children[0],
    textItemParagraph = processBlock.children[2].children[1]

console.log("processBlock", processBlock,
    "processImg", processImg,
    "process__line", process__line,
    "textItemTitle", textItemTitle,
    "textItemParagraph", textItemParagraph
    )

let scrollLock = "height: 876px; overflow: hidden;"
let scrollUnlock = ""

let imgArray = [
    "http://localhost:8000/static/images/process/process1.jpg",
    "http://localhost:8000/static/images/process/process2.jpg",
    "http://localhost:8000/static/images/process/process3.jpg",
    "http://localhost:8000/static/images/process/process4.jpg"
];

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

// let elementsForChanging = [
//
// ]

let counter = 0
let parasiteCounter = 0

let onScrollHandler = function(e) {
    let process_img_src = process_img.src
    console.log(window.pageYOffset, "window.pageYOffset")

    if (window.pageYOffset > 500 && window.pageYOffset < 1000) {
        counter = setCounter(e.deltaY, counter)
        body.style.cssText = scrollLock;
    }

    if (counter > 4 || counter < 0) {
            body.style.cssText = scrollUnlock;
            console.log("Unlock!")
    }
}

function changeContent(elements, counter, imgSourcesArray) {

}

function setCounter(deltaY, counter) {
    console.log("we are inside setCounter")
    if (deltaY > 0 && counter <= 4) {
        counter +=1
        console.log("increase counter")
        return counter
    } else if (deltaY < 0 && counter >= 0) {
        counter -= 1
        console.log("decrease Counter")
        return counter
    } else {
        return counter
    }
}

document.addEventListener ("wheel", onScrollHandler);