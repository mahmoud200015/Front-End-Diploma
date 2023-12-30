console.log("First Code".replace("i", "w"));
console.log("first");
console.log("Not in github");

let words = ["hello", "world", "leetcode"],
  chars = "welldonehoneyr";

let sum_len = 0;

words.forEach((word) => {
  let flag = true;
  for (let char of word) {
    if (
      chars.includes(char) &&
      countChars(char, word) <= countChars(char, chars)
    ) {
      flag = true;
      console.log(char);
    } else {
      flag = false;
      break;
    }
  }
  if (flag) {
    sum_len += word.length;
    console.log(word);
  }
});

function countChars(char, word) {
  return word.split("").filter((e) => e === char);
}

console.log(sum_len);

// Tutorial Git(1, )
// 1 probelm (3, )

console.log("Test: when you shut up pc is auto save is worked");

let str = "mad";

console.log(str.split("").sort())

