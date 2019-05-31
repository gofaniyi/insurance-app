<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <v-flex mt-3 mb-5>
            <div class="col-sm-10">
                <h2 v-if="currentRiskType">{{currentRiskType.name}} >> Risks</h2>
            </div>
        </v-flex>
        <v-flex mt-4>
            <v-btn v-if="currentRiskType" color="primary" :to="`/risks/add?riskTypeId=`+currentRiskType.id">Add New Risk</v-btn>
        </v-flex>
      </div>
      <v-flex mt-4>
          <v-data-table v-if="currentRiskType"
            :headers="headers"
            :items="currentRiskType.risks"
            class="elevation-1"
        >
            <template v-slot:items="props">
              <td v-for="(header, index) in headers" :key=index>
                {{ props.item.data[header.value] }}
              </td>
            </template>
        </v-data-table>
      </v-flex>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        headers: [],
        currentRiskType: null,
    };
  },
  methods: {
      getARiskType() {
            let state = this.$store.state;
            let path = `${state.api}` + '/risk-types/' + this.$route.params.id;
            let headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + state.user.token
            };
            return axios.get(path, {headers: headers})
                .then(res => {
                    let data = res.data.data;
                    this.currentRiskType = data;

                  
                    let tableHeaders = [];

                    this.currentRiskType.customAttributes.forEach(function(attribute){
                      tableHeaders.push({
                        text: attribute.label,
                        align: 'left',
                        value: attribute.key,
                        sortable: false,

                      })
                    })
                    this.headers = tableHeaders;
                })
                .catch((error) => {
                });
        },
  },
  created () {
        this.getARiskType();
    }
};
</script>