<template>
    <div class="container">
         <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
            <div v-if="!isAddLocation">
                <ul v-if="isShowLocation">
                    <li><router-link to="/">Accueil</router-link></li>
                    <li @click="isShowLocation = false"><a>Gestion des positions</a></li>
                    <li class="is-active"><a href="#" aria-current="page">Modification de {{location.name}}</a></li>
                </ul>
                <ul v-if="!isShowLocation">
                    <li><router-link to="/">Accueil</router-link></li>
                    <li class="is-active"><a href="#">Gestion des positions</a></li>
                </ul>
            </div>
            <ul v-if="isAddLocation">
                <li><router-link to="/">Accueil</router-link></li>
                <li><a href="#">Gestion des positions</a></li>
                <li class="is-active"><a href="#">Ajout d'une position</a></li>
            </ul>
        </nav>

  <!-- Ajout d'un type -->

        <template v-if="isAddLocation">
            <section>
                <hr>
                <div class="modal-card" style="width: auto">
                    <div>
                        <section class="modal-card-body">
                            <b-field label="Nom">
                                <b-input
                                    type="text"
                                    v-model="newLocation.name"
                                    placeholder="Nom du type"
                                    required>
                                </b-input>
                            </b-field>
                        </section>
                        <footer class="modal-card-foot">
                            <button class="button is-primary" @click="addLocation">Valider</button>
                            <b-button @click="isAddLocation = false">Annuler</b-button>
                        </footer>
                    </div>
                    <br>
                </div>
                    
            </section>
        </template>

        <!-- Modification d'un équipement -->

        <div class="notification" v-if="location && isShowLocation" >
            <h1 class="name is-2">Modification de " {{location.name}} " </h1>
            
            <div class="columns">
                <div class="column">
                    <b-field label="Nom du location de l'équipement">
                        <b-input v-model="location.name"></b-input>
                    </b-field>
                    <b-field grouped group-multiline>
                        <b-button location="is-primary" @click="updateLocation(location)">Modifier</b-button>
                        <b-button @click="isShowLocation = false">Annuler</b-button>
                    </b-field>
                </div>
            </div>
        </div>

        <!-- Chargement lors de la sauvegarde -->

        <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>


        <!-- Affichage du tableau des locations d'équipements -->

        <section v-if="!isShowLocation">
            <hr>

            <div class="columns">
                <div class="column is-2">
                    <b-button
                        v-if="isAddLocation == false"
                        icon-left="plus" @click="isAddLocation = true">
                        Ajouter une position
                    </b-button>
                </div>
                <div class="column">
                    <!-- Confirmation suppression -->
                    <div class="has-text-right" v-if="isDelete">
                        <span>
                            <button class="button is-danger" @click="deleteLocation(idEqToDel)">Confirmation suppression</button>
                        </span>
                        &nbsp;
                        <span>
                            <button class="button" @click="isDelete = false">Annuler</button>
                        </span>
                    </div>
                </div>
            </div>
            
            <hr>
            <b-field grouped group-multiline v-if="isAddLocation == false">
                <b-select v-model="defaultSortDirection">
                    <option value="asc">Tri: Croissant</option>
                    <option value="desc">Tri: Décroissant</option>
                </b-select>
                <b-select v-model="perPage" :disabled="!isPaginated">
                    <option value="5">5 par page</option>
                    <option value="10">10 par page</option>
                    <option value="15">15 par page</option>
                    <option value="20">20 par page</option>
                </b-select>
                <div class="control is-flex">
                    <b-switch v-model="isPaginated">Pagination</b-switch>
                </div>
            </b-field>

            <b-table
                v-if="isAddLocation == false"
                :data="locations"
                :paginated="isPaginated"
                :per-page="perPage"
                ref="table"
                :current-page.sync="currentPage"
                :pagination-simple="isPaginationSimple"
                :default-sort-direction="defaultSortDirection"
                default-sort="name"
                aria-next-label="Page suivante"
                aria-previous-label="Page précedente"
                aria-page-label="Page"
                aria-current-label="Page actuelle">

                <template slot-scope="props">
                    <b-table-column field="name" label="Libellé" sortable>
                        {{ props.row.name }}
                    </b-table-column>
                    <b-table-column sortable centered>
                        <b-field grouped group-multiline>
                            <div class="control is-flex">
                                <button class="button is-warning" @click="getLocation(props.row.id); isShowLocation = true"><i class="fas fa-edit"></i></button>
                            </div>
                            <div>
                                <button class="button is-danger" @click="callDelete(props.row.id)"><i class="fas fa-trash"></i></button>
                            </div>
                        </b-field>
                    </b-table-column>
                </template>
            </b-table>
        </section>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
    data() {
        return {
            data:[],
            idEqToDel:'',
            error: false, 
            isPaginated: true,
            isPaginationSimple: false,
            defaultSortDirection: 'asc',
            currentPage: 1,
            perPage: 5,
            defaultOpenedDetails: [1],
            showDetailIcon: true,
            isDelete: false,
            isAddLocation: false,
            isShowLocation: false,
            date: new Date(),
            isLoading: false,
            isFullPage: true,
            errors:'',
            newLocation:{
                name:'',
            }
        }
    },
    computed: mapState({
        locations: state => state.location.locations,
        location: state => state.location.location
    }),
    methods: {
        addLocation(){
            this.$store.dispatch('location/addLocation', this.newLocation)
            this.newLocation = { name:''}
            this.errors = this.$store.dispatch('location/getErrors')
    
            if(this.errors == 400 | this.errors == 500){
                this.$notification.open({
                    duration: 500,
                    message: `Un problème est survenu lors de l'ajout, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else{
                this.isLoading = true
                setTimeout(() => {
                    this.$store.dispatch('location/getLocations');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.isShowLocation = false
                    this.isAddLocation = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Enregistrement effectué avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
        },
        getLocation(payload){
            this.$store.dispatch('location/getLocation', payload)
        },
        callDelete(id){
            this.idEqToDel = id
            this.isDelete = true
        },
        deleteLocation(payload){
            this.$store.dispatch('location/deleteLocation', payload)
            this.isDelete = false
            this.errors = this.$store.dispatch('location/getErrors')
            console.log(this.errors)
            if(this.errors != 400 | this.errors !=500){
                setTimeout(() => {
                    this.$store.dispatch('location/getLocations');       
                    //location.reload()
                    this.$el.textContent
                    this.isDelete = false
                    this.isLoading = false
                    this.isShowLocation = false
                    this.isAddLocation = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Suppression effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)   
            }
            else
            {
                this.$notification.open({
                    duration: 5000,
                    message: `Suppression impossible, l'équipement est utilisé par une réservation`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
        },
        updateLocation(payload){
            this.$store.dispatch('location/updateLocation', payload)
            this.errors = this.$store.dispatch('location/getErrors')
            if(this.errors == 0){
                this.$notification.open({
                    duration: 20000,
                    message: `Un problème est survenu lors de la mise à jour, veuillez reessayer`,
                    position: 'is-bottom-right',
                    type: 'is-danger',
                    hasIcon: true
                })
            }
            else
            {
                this.isLoading = true
                setTimeout(() => {
                    this.$store.dispatch('location/getLocations');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.isShowLocation = false
                    this.$notification.open({
                        duration: 5000,
                        message: `Mise à jour effectuée avec succès`,
                        position: 'is-bottom-right',
                        type: 'is-success',
                        hasIcon: true
                    })
                }, 500)
            }
        }
        ,
        //Pour la liste déroulante de description
        toggle(row) {
            this.$refs.table.toggleDetails(row)
        }
    },
    created() {
        this.$store.dispatch('location/getLocations');
    }
}
</script>
