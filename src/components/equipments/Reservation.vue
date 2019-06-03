<template>
    <div class="container" @mouseenter="refresh">
        <hr>
        <hr>
        <!-- Breadcrumb -->
        <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
            <div class="level">
                <div class="level-left">
                    <div v-if="!isAdding">
                        <ul v-if="isUpdate">
                            <li><router-link to="/">Accueil</router-link></li>
                            <li @click="isUpdate = false"><a>Gestion des Réservations</a></li>
                            <li class="is-active"><a href="#" aria-current="page">Modification de la reservation N° {{reservation.id}}</a></li>
                        </ul>
                        <ul v-if="!isUpdate">
                            <li><router-link to="/">Accueil</router-link></li>
                            <li class="is-active"><a href="#">Gestion des Réservations</a></li>
                        </ul>
                    </div>
                    <ul v-if="isAdding">
                        <li><router-link to="/">Accueil</router-link></li>
                        <li><a href="#">Gestion des Réservations</a></li>
                        <li class="is-active"><a href="#">Ajout d'une réservation</a></li>
                    </ul>
                </div> 
                <!-- <div class="level-right">
                    <button class="button is-link" @click="refresh">Actualiser</button>
                </div> -->
            </div>
        </nav>

        <!-- Ajout d'un équipement -->

        <template v-if="isAdding">
            <section>
                <hr>
                <div class="modal-card" style="width: auto">
                    <div>
                        <section class="modal-card-body">
                            <div class="columns">
                                <div class="column">
                                    <b-field label="Equipement" type="is-fullwidth">
                                        <b-select placeholder="Selectionnez l'équipement" v-model="reservation.equipment_id" aria-required="true">
                                            <option v-for="equipment in equipments" :value="equipment.id">{{equipment.name}}</option>
                                        </b-select>
                                    </b-field>
                                    <b-field label="Période de réservation" aria-required="true">
                                        <date-range-picker v-model="range" :options="options"/>
                                    </b-field>
                                        <p class="help has-text-danger" v-if="validationRangeError">L'équipement est déjà réservé pendant cette période.</p>

                                </div>
                                <div class="column">
                                    <b-field label="Motif de la réservation">
                                        <b-input
                                            type="textarea"
                                            v-model="reservation.motif"
                                            placeholder="Motif de la réservation"
                                            required>
                                        </b-input>
                                    </b-field>
                                        <p class="help has-text-danger" v-if="validationMotifError">Veuillez spécifier un motif.</p>
                                </div>
                            </div>
                        </section>
                        <footer class="modal-card-foot">
                            <button class="button is-primary" @click="addReservation">Valider</button>
                            <b-button @click="cancel">Annuler</b-button>
                        </footer>
                    </div>
                    <br>
                </div>
                    
            </section>
        </template>

        <!-- Modification d'un équipement -->

        <div class="notification" v-if="reservation && isUpdate" >
            <h1 class="title is-2">Modification de la réservation N° " {{reservationOne.id}} " </h1>
            
            <section class="modal-card-body">
                <div class="columns">
                    <div class="column">
                        <b-field label="Equipement" type="is-fullwidth">
                            <b-select placeholder="Selectionnez l'équipement" v-model="reservation.equipment_id" aria-required="true">
                                <option v-for="equipment in equipments" :value="equipment.id">{{equipment.name}}</option>
                            </b-select>
                        </b-field>
                        <b-field v-if="reservation.status== 0">
                            <b-checkbox v-model="showRange"
                                native-value="yes">
                                Modifier la période de réservation
                            </b-checkbox>
                            <pre>[Début : {{reservation.start}} - Fin : {{reservation.end}}]</pre>
                        </b-field>

                        <div class="columns">
                            <div class="column">
                                <b-field v-if="reservation.status == 0">
                                    <b-checkbox v-model="showStatus"
                                        native-value="yes">
                                        Modifier le statut
                                    </b-checkbox>
                                    <pre v-if="reservation.status == 0 ">[Statut: En cours]</pre>
                                    <pre v-if="reservation.status == 1 ">[Statut: Terminé]</pre>
                                </b-field>
                                <b-field label="Statut" type="is-fullwidth" v-if="showStatus">
                                    <b-select placeholder="Statut de la réservation" v-model="reservation.status" aria-required="true">
                                        <option v-for="stat in status" :value="stat.code">{{stat.lib}}</option>
                                    </b-select>
                                </b-field>
                            </div>
                            <div class="column" v-if="reservation.status == 0">
                                <b-field>
                                    <br>
                                    <b-field label="Nouvelle période" aria-required="true" v-if="showRange">
                                        <date-range-picker v-model="range" :options="options"/>
                                    </b-field>
                                </b-field>
                            </div>
                        </div>
                    </div>
                    <div class="column" v-if="reservation.status == 0">
                        <b-field label="Motif de la réservation">
                            <b-input
                                type="textarea"
                                v-model="reservation.motif"
                                placeholder="Motif de la réservation"
                                required>
                            </b-input>
                        </b-field>
                    </div>
                </div>
            </section>
            <br>
            <b-field grouped group-multiline>
                <b-button type="is-primary" @click="updateReservation(reservation)">Modifier</b-button>
                <b-button @click="isUpdate = false">Annuler</b-button>
            </b-field>
        </div>

        <!-- Chargement lors de la sauvegarde -->

        <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
        
        <!-- Affichage du tableau des Réservations -->

        <section v-if="!isUpdate">
            <hr>

            <article class="message is-warning" v-if="equipments.length == 0">
                <div class="message-body has-text-centered">
                    Veuillez ajouter un <strong>équipement</strong> pour pouvoir faire une réservation
                </div>
            </article>
            
            <div class="columns">
                <div class="column is-2">
                    <b-button
                        v-if="isAdding == false && equipments.length != 0"
                        icon-left="plus" @click="isAdding = true">
                        Ajouter une réservation
                    </b-button>
                    
                </div>
                <div class="column">
                    <!-- Confirmation suppression -->
                    <div class="has-text-right" v-if="isDelete">
                        <span>
                            <button class="button is-danger" @click="deleteReservation(idEqToDel)">Confirmation suppression</button>
                        </span>
                        &nbsp;
                        <span>
                            <button class="button" @click="isDelete = false">Annuler</button>
                        </span>
                    </div>
                </div>
            </div>
            
            <hr>
            <b-field label="Filtre par nom d'équipement" v-if="isAdding == false">
                <b-input v-model="search"></b-input>                               
            </b-field>
            <b-field grouped group-multiline v-if="isAdding == false">
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
                <div class="control">
                    <b-switch v-model="showDetailIcon">Détail des reservations</b-switch>
                </div>
            </b-field>

            <b-table
                v-show="isAdding == false && filterReservations"
                :data="isEmpty ? [] : filterReservations"
                :paginated="isPaginated"
                :per-page="perPage"
                :opened-detailed="defaultOpenedDetails"
                ref="table"
                detailed
                detail-key="id"
                @details-open="(row, index) => $toast.open(`Expanded ${row.id}`)"
                :show-detail-icon="showDetailIcon"
                :current-page.sync="currentPage"
                :pagination-simple="isPaginationSimple"
                :default-sort-direction="defaultSortDirection"
                default-sort="name"
                aria-next-label="Page suivante"
                aria-previous-label="Page précedente"
                aria-page-label="Page"
                aria-current-label="Page actuelle">

                <template slot-scope="props">
                    <b-table-column field="equipment_id.name" label="Equipement" sortable centered>
                        <template v-if="showDetailIcon">
                            {{ props.row.equipment_id.name }}
                        </template>
                        <template v-else>
                            <a @click="toggle(props.row)">
                               {{ props.row.equipment_id.name }}
                            </a>
                        </template>
                    </b-table-column>

                    <b-table-column field="start" label="Date début" sortable centered>
                        <span class="tag is-success">
                            {{ new Date(props.row.start).toLocaleDateString() }}
                        </span>
                    </b-table-column>

                    <b-table-column field="end" label="Date fin" sortable centered>
                        <span class="tag is-info">
                            {{ new Date(props.row.end).toLocaleDateString() }}
                        </span>
                    </b-table-column>
                    <b-table-column field="status" label="Statut" sortable centered>
                        <p v-if="props.row.status == 1">
                            Terminé
                        </p>
                        <p v-else>
                            En cours
                        </p>
                    </b-table-column>
                    <b-table-column field="user_id.username" label="Réservé par" sortable centered>
                        {{ props.row.user_id.username }}
                    </b-table-column>

                    <b-table-column sortable centered>
                        <b-field grouped group-multiline>
                            <div class="control is-flex">
                                <button class="button is-warning" @click="getReservation(props.row.id); isUpdate = true"><i class="fas fa-edit"></i></button>
                            </div>
                            <div>
                                <button class="button is-danger" @click="callDelete(props.row.id)"><i class="fas fa-trash"></i></button>
                            </div>
                        </b-field>
                    </b-table-column>
                </template>

                <template slot="detail" slot-scope="props">
                    <article class="media">
                        <div class="media-content">
                            <div class="content">
                                <p>
                                    <strong>Motif de la réservation :</strong> {{props.row.motif}}
                                </p>
                            </div>
                        </div>
                    </article>
                </template>

                <!-- isEmpty -->
                <template slot="empty">
                    <section class="section">
                        <div class="content has-text-grey has-text-centered">
                            <p>
                                <b-icon
                                    icon="emoticon-sad"
                                    size="is-large">
                                </b-icon>
                            </p>
                            <p>Rien par ici.</p>
                        </div>
                    </section>
                </template>
            </b-table>
        </section>
    </div>
</template>

<script>
import moment from 'moment'
export default {
    data() {
        return {
            //Props for datatable
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
            //Props to show or hide components
            isDelete: false,
            isAdding: false,
            isUpdate: false,
            showRange: "",
            showStatus:"",

            //Validation
            validationRangeError: false,
            validationMotifError: false,

            date: new Date(),


            reservation:{
                start: '',
                end: '',
                status: '',
                motif: '',
                equipment_id: '',
                user_id: ''
            },
            reservationOne:[],
            isLoading: false,
            isFullPage: true,
            errors:'',
            search:'',
            isEmpty: false,
            range: ["",""],
            rangeOne: ["",""],
            options: {
                minDate: moment()
            },
            status:[
                {
                    code: 0,
                    lib: "En cours"
                },
                {
                    code: 1,
                    lib: "Terminé"
                }
            ],
            statusOne:""
        }
    },
    computed:{
        filterReservations(){
            if (this.$store.state.reservations.reservations){
                return this.$store.state.reservations.reservations.filter((key)=>{
                    if(key.equipment_id.name)
                    return key.equipment_id.name.match(this.search)
                })
            }
            else{
                this.isEmpty = true
            }
        },
        equipments(){
            return this.$store.state.equipments.equipments
        }
    },
    methods: {
        refresh(){
            this.$store.dispatch('reservations/getReservations');
            this.$store.dispatch('equipments/getEquipments');
            this.$store.dispatch('reservations/getErrors')
        },
        cancel(){
            this.isAdding = false
            this.$store.dispatch('reservations/getReservations');
            this.$store.dispatch('equipments/getEquipments');
            this.errors = this.$store.dispatch('reservations/getErrors')
        },
        resetAll(){
            this.errors = ''
            this.reservation = {
                start: '',
                end: '',
                status: '',
                motif: '',
                equipment_id: '',
                user_id: ''
            }
            this.range=["",""]
            this.isLoading = false
            this.isAdding = false
        },
        errorMessage(){
            this.errors = this.$store.dispatch('reservations/getErrors')
            this.$notification.open({
                duration: 5000,
                message: `Un problème est survenu lors de l'ajout, veuillez reessayer`,
                position: 'is-bottom-right',
                type: 'is-danger',
                hasIcon: true
            })
        },
        successMessage(){
            this.errors = this.$store.dispatch('reservations/getErrors')
            this.$notification.open({
                duration: 5000,
                message: `Enregistrement effectué avec succès`,
                position: 'is-bottom-right',
                type: 'is-success',
                hasIcon: true
            }) 
        },
        addReservation(){
   
            this.reservation.start = (this.range[0])
            this.reservation.end = this.range[1]
            this.reservation.status = "0";
            this.reservation.user_id = "1";
            // Validation

            var res = this.getReservationByEquipment(this.reservation.equipment_id)
            //var res_date = res.start.split(/\//).reverse().join('/');
            console.log(res.start)
            var newdate = this.reservation.start.split("/").reverse().join("-");

            console.log(newdate)
            if (res.start == newdate){
                this.validationRangeError = true
            }
            else if (newdate < res.end ){
                this.validationMotifError = false                
                this.validationRangeError = true
            }
            else if(!this.reservation.motif){
                this.validationMotifError = false                
                this.validationMotifError = true
            }
            else
            {
                this.validationRangeError = false
                this.validationMotifError = false                
                
                this.$store.dispatch('reservations/addReservation', this.reservation)
                this.$store.dispatch('reservations/getErrors')
                this.isLoading = true
                setTimeout(() => {
                    this.$store.dispatch('reservations/getErrors').then( body => {
                        if (body == 400){
                            this.errorMessage()
                            this.isLoading = false
                        }
                        else{
                        this.resetAll()
                        this.successMessage()
                        }
                        this.errors = this.$store.dispatch('reservations/getErrors')
                    })            
                },2000)

                if (this.errors == 201)
                {
                    this.resetAll()
                    this.successMessage()
                }
            }
        },
        getReservation(payload){

            this.reservationOne = this.filterReservations.find(fruit => fruit.id === payload)
            console.log(this.reservationOne)
            this.range = [this.reservationOne.start, this.reservationOne.end]
            this.reservation.id = this.reservationOne.id
            this.reservation.start = this.reservationOne.start
            this.reservation.end = this.reservationOne.end
            this.rangeOne = [this.reservationOne.start, this.reservationOne.end]
            console.log(this.range);            
            this.reservation.status = this.reservationOne.status
            this.reservation.motif = this.reservationOne.motif
            this.reservation.equipment_id = this.reservationOne.equipment_id.id
            this.reservation.user_id = this.reservationOne.user_id.id
        },
        getReservationByEquipment(id){
            return this.filterReservations.find(fruit => fruit.equipment_id.id === id)
        },
        callDelete(id){
            this.idEqToDel = id
            this.isDelete = true
        },
        deleteReservation(payload){
            this.$store.dispatch('reservations/deleteReservation', payload)
            this.isDelete = false
            this.errors = this.$store.dispatch('reservations/getErrors')
            //console.log(this.errors)
            if(this.errors != 400 | this.erros != 500){
                setTimeout(() => {
                    this.$store.dispatch('reservations/getReservations');
                    //location.reload()
                    this.$el.textContent
                    this.isDelete = false
                    this.isLoading = false
                    this.isUpdate = false
                    this.isAdding = false
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
        updateReservation(payload){
            //console.log(payload)
            this.reservation.start = this.range[0]
            this.reservation.end = this.range[1]

            console.log(this.reservation.start)
            this.$store.dispatch('reservations/updateReservation', this.reservation)
            this.errors = this.$store.dispatch('reservations/getErrors')
            if(this.errors == 400 | this.errors == 500){
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
                    this.$store.dispatch('reservations/getReservations');
                    //location.reload()
                    this.$el.textContent
                    this.isLoading = false
                    this.isUpdate = false
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
        },
    },
    created() {
        this.$store.dispatch('reservations/getReservations');
        this.$store.dispatch('equipments/getEquipments');
    }
}
</script>