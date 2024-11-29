/*eslint-disable*/
export default function getStudentIdsSum(objects_array) {
  if (!Array.isArray(objects_array)) return 0;
  return objects_array.reduce((acc, object) => acc + object.id, 0);
}