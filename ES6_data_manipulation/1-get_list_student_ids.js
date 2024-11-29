/*eslint-disable*/
export default function getListStudentIds(objects_array) {
  if (!Array.isArray(objects_array)) return [];
  return objects_array.map((object) => object.id);
}