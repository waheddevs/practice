/* A-TASK:
SAVOL: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

// Masalaning yechimi:
function countLetter(a, shaxzoda) {
  let count = 0;
  for (let letter of shaxzoda) {
    if (letter === a) {
      count++;
    }
  }

return count;
}

console.log(countLetter("a", "shaxzoda"));
console.log(countLetter("b", "abduvohid"));