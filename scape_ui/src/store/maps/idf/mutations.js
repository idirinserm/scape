import { SET_GEOJSON_DATA } from "./mutations_types";

export default {
  [SET_GEOJSON_DATA](state, payload) {
    state.geojsonData = payload.geojsonData;
    state.jsonCoordinates = payload.jsonCoordinates;
    state.geojsonFeature = payload.geojsonFeature;
  },
};
