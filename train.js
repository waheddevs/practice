/* A-TASK:
SAVOL: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

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