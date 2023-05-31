export default {
  getGeojsonData(state) {
    return state.geojsonData;
  },
  getCoordinates(state){
    return state.jsonCoordinates;
  },
  getError(state) {
    return state.error;
  },
};
