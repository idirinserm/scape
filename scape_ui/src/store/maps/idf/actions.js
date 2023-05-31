import axios from "axios";
import { SET_GEOJSON_DATA } from "./mutations_types";

export default {
  async fetchGeojson({ commit }) {
    try {
      const response = await axios.get("http://localhost:8000/commune/422/");
      const geojsonData = response.data;
      const jsonCoordinates = geojsonData.geometry.coordinates;

      const geoConf = {
        type: "FeatureCollection",
        features: [
          { type: "Feature", geometry: geojsonData.geojson, id: "Nom" },
        ],
      };

      console.log(jsonCoordinates);

      commit(SET_GEOJSON_DATA, {
        geojsonData,
        geojsonFeature: geoConf,
        jsonCoordinates: jsonCoordinates,
      });
    } catch (error) {
      console.error(error);
    }
  },
};
