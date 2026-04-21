/* C-TASK:
Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
*/


// Masalaning yechimi:
function checkContent(first, second) {
  if(first.length !== second.length) return false;

  let a = first.split('').sort().join('');
  let b = second.split('').sort().join('');

  return a === b;
}

console.log(checkContent('olma', 'almo'));
console.log(checkContent('behi', 'bhe'));





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