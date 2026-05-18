/* N-TASK (NodeJS)

Shunday function yozing, u raqamlardan tashkil topgan array qabul qilsin va array ichidagi har bir raqam uchun raqamni ozi va hamda osha raqamni kvadratidan tashkil topgan object hosil qilib, hosil bolgan objectlarni array ichida qaytarsin.
MASALAN: getSquareNumbers([1, 2, 3]) return [{number: 1, square: 1}, {number: 2, square: 4}, {number: 3, square: 9}];
*/


// Masalaning yechimi:
function getSquareNumbers(numbers) {
  const result = [];
  for (let num of numbers) {
    result.push({ number: num, square: num * num });
  }
  return result;
}

console.log(getSquareNumbers([8, 12, 5]));
console.log(getSquareNumbers([7, 4, 13]));







//==============================================================================================================================

/* L-TASK (NodeJS)

Shunday function yozing, u string qabul qilsin va string ichidagi hamma sozlarni chappasiga yozib va sozlar ketma-ketligini buzmasdan stringni qaytarsin.
MASALAN: reverseSentence("we like coding!") return "ew ekil gnidoc";
*/

/*
// Masalaning yechimi:
function reverseSentence(text) {

    const words = text.split(" ");
    const reversedWords = words.map(word => {
        return word.split("").reverse().join("");
    });

    return reversedWords.join(" ");
}

console.log(reverseSentence("Aldaysan-ku Sardor"));
console.log(reverseSentence("Nimo'lyapti?"));
*/



//==============================================================================================================================

/* J-TASK (NodeJS)

Shunday function yozing, u parametridagi array ichida eng kop takrorlangan raqamni topib qaytarsin.
MASALAN: majorityElement([1,2,3,4,5,4,3,4]) return 4
*/

/*
// Masalaning yechimi:
function majorityElement(numbers) {
  const countMap = {};
  let majority = numbers[0];
  let maxCount = 1;
  for (let num of numbers) {
    countMap[num] = (countMap[num] || 0) + 1;
    if (countMap[num] > maxCount) {
      maxCount = countMap[num];
      majority = num;
    }
  }
  return majority;
}

console.log(majorityElement([12, 2, 8, 5, 8, 16, 8, 3]));
*/




//==============================================================================================================================

/* H-TASK (NodeJS)
shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
MASALAN: getPositive([1, -4, 2]) return qiladi "12"
*/

/*
// Masalaning yechimi:

function getPositive(numbers) {
  let result = '';
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > 0) {
      result += numbers[i];
    }
  }

  return result;
}

console.log(getPositive([-1, 2, -3, 4, -5]));
console.log(getPositive([-1, -9, 33, -4, 1]));
console.log(getPositive([21, 2, 35, 48]));
*/



//==============================================================================================================================

/* F-TASK
Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
MASALAN: getReverse("hello") return true return qiladi
*/

/*
// Masalaning yechimi:
function findDoublers(i) {
    const harf = new Set();
    for (let char of i) {
        if (harf.has(char)) {
            return true;
        }
        harf.add(char);
    }

    return false;
}

console.log(findDoublers("alla"));
console.log(findDoublers("yalla"));
console.log(findDoublers("olma"));
console.log(findDoublers("banan"));
*/



//==============================================================================================================================

/* E-TASK
Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
*/

/*
// Masalaning yechimi:
function getReverse(abc) {
  let result = ''
  for (let i = abc.length - 1; i >= 0; i--) {
    result += abc[i]
  }
  return result
}

console.log(getReverse('ARNOLD'))
console.log(getReverse('MARTIN'))
*/




//==============================================================================================================================

/* D-TASK
Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
*/

/*
// Masalaning yechimi:
function getHighestIndex(array) {
    let biggestOne = array[0];

    for (let i = 1; i < array.length; i++) {
        if (array[i] > biggestOne) {
            biggestOne = array[i];
        }
    }

    for (let i = 0; i < array.length; i++) {
        if (array[i] === biggestOne) {
            return i;
        }
    }
}

let result = getHighestIndex([3, 19, 9, 19, 4]);
console.log(result);
*/




//==============================================================================================================================

/* C-TASK:
Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
*/

/*
// Masalaning yechimi:
function checkContent(first, second) {
  if(first.length !== second.length) return false;

  let a = first.split('').sort().join('');
  let b = second.split('').sort().join('');

  return a === b;
}

console.log(checkContent('olma', 'almo'));
console.log(checkContent('behi', 'bhe'));
*/




//==============================================================================================================================

/* B-TASK:
SAVOL: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

/*
// Masalaning yechimi:
function countDigits(raqam) {
  let count = 0;
  for (let char of raqam) {
    if (char >= '0' && char <= '9') {
      count++;
    }
  }
  return count;
}


console.log(countDigits('dfj5fwG6'));
console.log(countDigits('dfj5f8wG6'));
console.log(countDigits('dfj5fwG640Ghjv7'));
*/




//==============================================================================================================================

/* A-TASK:
SAVOL: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

/*
// Masalaning yechimi:
function countLetter(b, abduvohid) {
  let count = 0;
  for (let letter of abduvohid) {
    if (letter === b) {
      count++;
    }
  }

return count;
}

console.log(countLetter("j", "jasur"));
console.log(countLetter("d", "abduvohid"));
*/