<template>
  <div>
    <input type="text" v-model="clientId">
    <button @click="gapiLoad()">gapi load</button>
    <input type="text" v-model="apiKey">
    <button @click="authenticate().then(loadClient)">authorize and load</button>
    <button @click="execute()">execute</button>
  </div>
</template>

<script src="https://apis.google.com/js/api.js"></script>
<script>
export default {
  data() {
    return {
      apiKey: '',
      clientId: '',
    }
  },
  methods: {
    authenticate() {
      return gapi.auth2
        .getAuthInstance()
        .signIn({
          scope:
            "https://www.googleapis.com/auth/analytics https://www.googleapis.com/auth/analytics.readonly",
        })
        .then(
          function () {
            console.log("Sign-in successful");
          },
          function (err) {
            console.error("Error signing in", err);
          }
        );
    },
    loadClient() {
      gapi.client.setApiKey(this.apiKey);
      return gapi.client
        .load(
          "https://content.googleapis.com/discovery/v1/apis/analyticsreporting/v4/rest"
        )
        .then(
          function () {
            console.log("GAPI client loaded for API");
          },
          function (err) {
            console.error("Error loading GAPI client for API", err);
          }
        );
    },
    execute() {
      return gapi.client.analyticsreporting.reports
        .batchGet({
          prettyPrint: true,
          resource: {
            reportRequests: [
              {
                viewId: "233136825",
                dateRanges: [
                  {
                    startDate: "2020-11-17",
                    endDate: "2020-11-17",
                  },
                ],
                dimensions: [
                  {
                    name: "ga:pageTitle",
                  },
                ],
                metrics: [
                  {
                    expression: "ga:pageviews",
                  },
                ],
                filtersExpression: "ga:pagePath==/product",
              },
            ],
          },
        })
        .then(
          function (response) {
            // Handle the results here (response.result has the parsed body).
            console.log("Response", response);
          },
          function (err) {
            console.error("Execute error", err);
          }
        );
    },
    gapiLoad() {
      console.log(this.clientId)
      gapi.load("client:auth2", function () {
        gapi.auth2.init({ client_id: this.clientId });
      }.bind(this));
    }
  },
};
</script>

<style>
</style>