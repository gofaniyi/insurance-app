<template>
  <v-container>
    <v-flex mt-3>
      <div class="col-sm-10">
        <h2>Risk Types</h2>
        <v-flex mt-4>
            <v-btn color="primary" to="/risk-types/add">Add New Risk Type</v-btn>
        </v-flex>
      </div>
    </v-flex>

    <v-container grid-list-md text-xs-center>

        <v-layout row wrap>
            <v-dialog v-model="dialog" persistent max-width="290">
              <v-card>
                <v-card-title class="body-2">Delete Risk Type</v-card-title>
                <v-divider></v-divider>
                <v-card-text>Do you want to remove this risk type?</v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn  color="primary darken-1" @click="deleteRiskType(selectedRiskType)">Yes</v-btn>
                  <v-btn color="grey darken-1" outline @click="dialog = false">No</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <v-flex v-for="riskType in riskTypes" v-bind:key="riskType.id" xs3>
                <v-card color="white darken-2" class="blue-grey--text">
                    <v-card-title primary-title>
                        <div class="text-lg-left">
                            <a class="risk-type" :href="`/risk-types/`+riskType.id+`/risks`" :id=riskType.id>
                              <div class="headline font-weight-bold">{{riskType.name}}</div>
                            </a>
                            <span class="grey--text">{{riskType.risksCount}} Risks Created</span>

                        </div>
                    </v-card-title>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn icon :to="`/risk-types/`+riskType.id+`/edit`">
                            <v-icon color="green">edit</v-icon>
                        </v-btn>
                          <v-btn icon>
                              <v-icon color="red" dark @click="openDialog(riskType.id)">delete</v-icon>
                          </v-btn>
                        
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
  </v-container>
</template>

<script>

export default {
  data() {
    return {
      dialog: false,
      selectedRiskType: null,
      };
    },
  computed: {
        riskTypes() {
            return this.$store.state.riskTypes;;
        }
    },
    mounted() {
        this.getRiskTypes();
    },
  methods: {
      getRiskTypes() {
        this.$store.dispatch('getRiskTypes');
      },
      openDialog (selected) {
        this.dialog = true;
        this.selectedRiskType = selected;
      },
      deleteRiskType (selected) {
        this.$store.dispatch('deleteRiskType', selected);
      }
  },
  watch: {
      dialog (val) {
        if (!val) return
      }
    }
};
</script>

<style scoped>
.risk-type{
  text-decoration: none
}

.risk-type:hover{
  text-decoration: underline
}
</style>