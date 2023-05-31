<template>
  <ol-map
    :loadTilesWhileAnimating="true"
    :loadTilesWhileInteracting="true"
    style="height: 100vh"
    ref="map"
  >
    <ol-view
      ref="view"
      :center="center"
      :rotation="rotation"
      :zoom="zoom"
      :projection="projection"
    />

    <!--        <ol-tile-layer>-->
    <!--          <ol-source-osm />-->
    <!--        </ol-tile-layer>-->

    <ol-interaction-select
      @select="featureSelected"
      :condition="selectCondition"
      :filter="selectInteactionFilter"
    >
      <ol-style>
        <ol-style-stroke color="white" :width="2"></ol-style-stroke>
        <ol-style-fill color="rgba(255,255,255,0.5)"></ol-style-fill>
      </ol-style>
    </ol-interaction-select>

    <ol-vector-layer>
      <ol-source-vector
        ref="nom"
        :url="url"
        :format="geoJson"
        :projection="projection"
      >
      </ol-source-vector>

      <ol-interaction-select
        @select="featureOnclick"
        :condition="onclickCondition"
        :filter="onclickInteactionFilter"
        ref="marker"
      >
        <ol-context-menu :items="contextMenuItems" />
        <ol-style>
          <ol-style-stroke color="blue" :width="2"></ol-style-stroke>
          <ol-style-fill color="rgba(255,255,255,0.5)"></ol-style-fill>
        </ol-style>
      </ol-interaction-select>

      <ol-style>
        <ol-style-stroke color="red" :width="0.5"></ol-style-stroke>
        <ol-style-fill color="rgba(255,255,255,0.1)"></ol-style-fill>
      </ol-style>
    </ol-vector-layer>
  </ol-map>
</template>

<script>
import { inject, ref } from "vue";

export default {
  name: "MapCom",
  data: () => ({
    active: false,
    dialog: false,
  }),
  setup() {
    const center = ref([2.3488, 48.8502]);
    const projection = ref("EPSG:4326");
    const zoom = ref(9.5);
    const rotation = ref(0);
    const radius = ref(20);
    const strokeWidth = ref(2);
    const strokeColor = ref("grey");
    const url = ref(import.meta.env.VITE_APP_ROOT_API + "commune/");

    const markers = ref(null);
    const view = ref(null);
    const Feature = inject("ol-feature");
    const Geom = inject("ol-geom");

    const format = inject("ol-format");
    console.log(format);
    const geoJson = new format.GeoJSON();
    console.log(geoJson);
    console.log(Feature);
    console.log(Geom);

    const selectConditions = inject("ol-selectconditions");
    const selectCondition = selectConditions.pointerMove;
    const onclickConditions = inject("ol-selectconditions");
    const onclickCondition = onclickConditions.click;
    const contextMenuItems = ref([]);

    const featureSelected = (event) => {
      console.log(event);
    };
    const featureOnclick = (event) => {
      console.log(event);
    };
    const selectInteactionFilter = (feature) => {
      return feature.values_.nom !== undefined;
    };

    const onclickInteactionFilter = (feature) => {
      contextMenuItems.value = [
        {
          text: feature.values_.nom,
          classname: "some-style-class", // add some CSS rules
          callback: (val) => {
            view.value.setCenter(val.coordinate);
          }, // `center` is your callback function
        },
        {
          text: feature.values_.insee,
          classname: "some-style-class", // add some CSS rules
        },
        {
          // text: "Add a Marker",
          classname: "some-style-class", // you can add this icon with a CSS class
          // instead of `icon` property (see next line)
          // icon: marker, // this can be relative or absolute
          callback: (val) => {
            console.log(val);
            let feature = new Feature({
              geometry: new Geom.Point(val.coordinate),
            });
            markers.value.source.addFeature(feature);
          },
        },
        "-", // this is a separator
      ];
      return feature.values_.nom !== undefined;
    };

    return {
      center,
      projection,
      zoom,
      rotation,
      radius,
      strokeWidth,
      strokeColor,
      selectCondition,
      onclickCondition,
      featureSelected,
      featureOnclick,
      selectInteactionFilter,
      onclickInteactionFilter,
      url,
      geoJson,
      contextMenuItems,
      markers,
      view,
    };
  },
};
</script>

<style>
.overlay-content {
  background: #efefef;
  box-shadow: 0 5px 10px rgb(2 2 2 / 20%);
  padding: 10px 20px;
  font-size: 16px;
}

.map {
  width: 100%;
  height: 400px;
}
.map:-webkit-full-screen {
  height: 100%;
  margin: 0;
}
.map:fullscreen {
  height: 100%;
}
.map .ol-rotate {
  top: 3em;
}
</style>
