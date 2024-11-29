/*eslint-disable*/
export default function hasArrayValues(set, array) {
  return array.every((element) => set.has(element));
}