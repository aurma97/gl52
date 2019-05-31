// <template>
//     <div class="container">
//         <hr>
//         <hr>
//         <!-- Breadcrumb -->
//         <nav class="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">     
//             <div class="level">
//                 <div class="level-left">
//                     <div v-if="!isComponentModalActive">
//                         <ul v-if="showReservation">
//                             <li><router-link to="/">Accueil</router-link></li>
//                             <li @click="showReservation = false"><a>Gestion des Réservations</a></li>
//                             <li class="is-active"><a href="#" aria-current="page">Modification de la reservation N° {{reservation.id}}</a></li>
//                         </ul>
//                         <ul v-if="!showReservation">
//                             <li><router-link to="/">Accueil</router-link></li>
//                             <li class="is-active"><a href="#">Gestion des Réservations</a></li>
//                         </ul>
//                     </div>
//                     <ul v-if="isComponentModalActive">
//                         <li><router-link to="/">Accueil</router-link></li>
//                         <li><a href="#">Gestion des Réservations</a></li>
//                         <li class="is-active"><a href="#">Ajout d'une réservation</a></li>
//                     </ul>
//                 </div> 
//                 <!-- <div class="level-right">
//                     <button class="button is-link" @click="refresh">Actualiser</button>
//                 </div> -->
//             </div>
//         </nav>

//         <!-- Ajout d'un équipement -->

//         <template v-if="isComponentModalActive">
//             <section>
//                 <hr>
//                 <div class="modal-card" style="width: auto">
//                     <div>
//                         <section class="modal-card-body">
//                           <v-range-selector
//                             :start-date.sync="reservation.start"
//                             :end-date.sync="reservation.end"
//                             />
                            
//                             <div class="field">
//                                 <label class="label">Dernière maintenance</label>
//                                 <div class="control has-icons-right">
//                                     <input class="input" type="text" v-model="reservation.status">
//                                     <span class="icon is-small is-right">
//                                     <i class="fas fa-calendar"></i>
//                                     </span>
//                                 </div>
//                             </div>

//                             <b-field label="Description">
//                                 <b-input
//                                     type="textarea"
//                                     v-model="reservation.motif"
//                                     placeholder="Détails sur l'équipement"
//                                     required>
//                                 </b-input>
//                             </b-field>
//                             <b-field label="Conditions d'utilisation">
//                                 <b-input
//                                     type="textarea"
//                                     v-model="reservation.equipment_id"                        
//                                     required>
//                                 </b-input>
//                             </b-field>                
//                         </section>
                        
//                         <footer class="modal-card-foot">
//                             <button class="button is-primary" @click="addReservation">Valider</button>
//                             <b-button @click="isComponentModalActive = false">Annuler</b-button>
//                         </footer>
//                     </div>
//                     <br>
//                 </div>
                    
//             </section>
//         </template>

//         <!-- Modification d'un équipement -->

//         <div class="notification" v-if="reservation && showReservation" >
//             <h1 class="title is-2">Modification de " {{equipment.name}} " </h1>
            
//             <div class="columns">
//                 <div class="column">
//                     <b-field label="Nom de l'équipement">
//                         <b-input v-model="equipment.name"></b-input>
//                     </b-field>
//                     <b-field label="Description">
//                         <b-input maxlength="200" v-model="equipment.description" type="textarea"></b-input>
//                     </b-field>
//                     <b-field label="Conditions d'utilisation">
//                         <b-input maxlength="100" v-model="equipment.use_cond" type="textarea"></b-input>
//                     </b-field>
//                 </div>
//                 <div class="column">
//                     <!-- <b-field label="Type d'équipement" type="is-fullwidth">
//                         <b-select placeholder="Select a character" v-model="equipment.type_id">
//                             <option :value="equipmentOne.type_id.id" selected>
//                                 {{equipmentOne.type_id.title}}
//                             </option>
//                             <option v-for="type in types" v-if="type.title != equipmentOne.type_id.title" :value="type.id">{{type.title}}</option>
//                         </b-select>
//                     </b-field>
//                     <b-field label="Localisation" type="is-fullwidth">
//                         <b-select :placeholder="equipment.location.name" v-model="equipment.location">
//                             <option :value="equipmentOne.location.id" selected>
//                                 {{equipmentOne.location.name}}
//                             </option>
//                             <option v-for="location in locations" v-if="location.name != equipmentOne.location.name" :value="location.id">{{location.name}}</option>
//                         </b-select>
//                     </b-field> -->
//                     <div class="field">
//                         <label class="label">Date d'acquisition</label>
//                         <div class="control has-icons-right">
//                             <input class="input" type="date" v-model="equipment.date_purchase">
//                             <span class="icon is-small is-right">
//                             <i class="fas fa-calendar"></i>
//                             </span>
//                         </div>
//                     </div>
//                     <div class="field">
//                         <label class="label">Dernière maintenance</label>
//                         <div class="control has-icons-right">
//                             <input class="input" type="date" v-model="equipment.last_check">
//                             <span class="icon is-small is-right">
//                             <i class="fas fa-calendar"></i>
//                             </span>
//                         </div>
//                     </div>
//                     <b-field grouped group-multiline>
//                         <b-button type="is-primary" @click="updateReservation(equipment)">Modifier</b-button>
//                         <b-button @click="showReservation = false">Annuler</b-button>
//                     </b-field>
//                 </div>
//             </div>
//         </div>

//         <!-- Chargement lors de la sauvegarde -->

//         <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
        
//         <!-- Affichage du tableau des Réservations -->
        

//         <section v-if="!showReservation">
//             <hr>

//             <article class="message is-warning">
//                 <div class="message-body has-text-centered">
//                     Veuillez ajouter un <strong>Type d'équipement</strong> et une <strong>localisation</strong> pour pouvoir rajouter un équipement
//                 </div>
//             </article>
            
//             <div class="columns">
//                 <div class="column is-2">
//                     <b-button
//                         v-if="isComponentModalActive == false"
//                         icon-left="plus" @click="isComponentModalActive = true">
//                         Ajouter une réservation
//                     </b-button>
                    
//                 </div>
//                 <div class="column">
//                     <!-- Confirmation suppression -->
//                     <div class="has-text-right" v-if="isDelete">
//                         <span>
//                             <button class="button is-danger" @click="deleteReservation(idEqToDel)">Confirmation suppression</button>
//                         </span>
//                         &nbsp;
//                         <span>
//                             <button class="button" @click="isDelete = false">Annuler</button>
//                         </span>
//                     </div>
//                 </div>
//             </div>
            
//             <hr>
//             <b-field label="Filtre par nom d'équipement" v-if="isComponentModalActive == false">
//                 <b-input v-model="search"></b-input>                               
//             </b-field>
//             <b-field grouped group-multiline v-if="isComponentModalActive == false">
//                 <b-select v-model="defaultSortDirection">
//                     <option value="asc">Tri: Croissant</option>
//                     <option value="desc">Tri: Décroissant</option>
//                 </b-select>
//                 <b-select v-model="perPage" :disabled="!isPaginated">
//                     <option value="5">5 par page</option>
//                     <option value="10">10 par page</option>
//                     <option value="15">15 par page</option>
//                     <option value="20">20 par page</option>
//                 </b-select>
//                 <div class="control is-flex">
//                     <b-switch v-model="isPaginated">Pagination</b-switch>
//                 </div>
//                 <div class="control">
//                     <b-switch v-model="showDetailIcon">Détail des reservations</b-switch>
//                 </div>
//             </b-field>

//             <b-table
//                 v-if="isComponentModalActive == false"
//                 :data="isEmpty ? [] : filterReservations"
//                 :paginated="isPaginated"
//                 :per-page="perPage"
//                 :opened-detailed="defaultOpenedDetails"
//                 ref="table"
//                 detailed
//                 detail-key="id"
//                 @details-open="(row, index) => $toast.open(`Expanded ${row.id}`)"
//                 :show-detail-icon="showDetailIcon"
//                 :current-page.sync="currentPage"
//                 :pagination-simple="isPaginationSimple"
//                 :default-sort-direction="defaultSortDirection"
//                 default-sort="name"
//                 aria-next-label="Page suivante"
//                 aria-previous-label="Page précedente"
//                 aria-page-label="Page"
//                 aria-current-label="Page actuelle">

//                 <template slot-scope="props">
//                     <b-table-column field="equipment_id.name" label="Equipement" sortable centered>
//                         <template v-if="showDetailIcon">
//                             {{ props.row.equipment_id.name }}
//                         </template>
//                         <template v-else>
//                             <a @click="toggle(props.row)">
//                                {{ props.row.equipment_id.name }}
//                             </a>
//                         </template>
//                     </b-table-column>

//                     <b-table-column field="start" label="Date début" sortable centered>
//                         <span class="tag is-success">
//                             {{ new Date(props.row.start).toLocaleDateString() }}
//                         </span>
//                     </b-table-column>

//                     <b-table-column field="end" label="Date fin" sortable centered>
//                         <span class="tag is-info">
//                             {{ new Date(props.row.end).toLocaleDateString() }}
//                         </span>
//                     </b-table-column>
//                     <b-table-column field="status" label="Statut" sortable centered>
//                         <p v-if="props.row.status == 1">
//                             Terminé
//                         </p>
//                         <p v-else>
//                             En cours
//                         </p>
//                     </b-table-column>
//                     <b-table-column field="user_id.username" label="Réservé par" sortable centered>
//                         {{ props.row.user_id.username }}
//                     </b-table-column>

//                     <b-table-column sortable centered>
//                         <b-field grouped group-multiline>
//                             <div class="control is-flex">
//                                 <button class="button is-warning" @click="getReservation(props.row.equipment_id.id); showReservation = true"><i class="fas fa-edit"></i></button>
//                             </div>
//                             <div>
//                                 <button class="button is-danger" @click="callDelete(props.row.id)"><i class="fas fa-trash"></i></button>
//                             </div>
//                         </b-field>
//                     </b-table-column>
//                 </template>

//                 <template slot="detail" slot-scope="props">
//                     <article class="media">
//                         <div class="media-content">
//                             <div class="content">
//                                 <p>
//                                     <strong>Motif de la réservation :</strong> {{props.row.motif}}
//                                 </p>
//                             </div>
//                         </div>
//                     </article>
//                 </template>

//                 <!-- isEmpty -->
//                 <template slot="empty">
//                     <section class="section">
//                         <div class="content has-text-grey has-text-centered">
//                             <p>
//                                 <b-icon
//                                     icon="emoticon-sad"
//                                     size="is-large">
//                                 </b-icon>
//                             </p>
//                             <p>Rien par ici.</p>
//                         </div>
//                     </section>
//                 </template>
//             </b-table>
//         </section>
//     </div>
// </template>

// <script>
// import VRangeSelector from 'vuelendar/components/vl-range-selector';
// import VDaySelector from 'vuelendar/components/vl-day-selector';


// export default {
//     components: {
//         VRangeSelector,
//         VDaySelector
//     },
//     data() {
//         return {
//             data:[],
//             idEqToDel:'',
//             error: false, 
//             isPaginated: true,
//             isPaginationSimple: false,
//             defaultSortDirection: 'asc',
//             currentPage: 1,
//             perPage: 5,
//             defaultOpenedDetails: [1],
//             showDetailIcon: true,
//             isDelete: false,
//             isComponentModalActive: false,
//             showReservation: false,
//             date: new Date(),
//             reservation:{
//                 id: '',
//                 start: '',
//                 end: '',
//                 status: '',
//                 motif: '',
//                 equipment_id: '',
//                 user_id: ''
//             },
//             reservationOne:[],
//             isLoading: false,
//             isFullPage: true,
//             errors:'',
//             search:'',
//             isEmpty: false,
//             range: {
//                 start: '',
//                 end: ''
//             }
            
//         }
//     },
//     computed:{
//         filterReservations(){
//             if (!this.reservations){
//                 this.isEmpty = true
//             }
//             return this.reservations.filter((reservation)=>{
//                 return reservation.equipment_id.name.match(this.search)
//             })
//         }, 
//         reservations(){
//             return this.$store.state.reservations.reservations
//         }
//     },
//     methods: {
//         refresh(){
//             this.$store.dispatch('reservations/getReservations');
//         },

//         addReservation(){
//             this.$store.dispatch('reservations/addReservation', this.equipment)
//             this.errors = this.$store.dispatch('reservations/getErrors')
//             // var error = this.errors.then( body => console.log( JSON.parse( body ) ) )
//             // console.log(error)
//             if(this.errors == 400 | this.errors == 500){
//                 this.$notification.open({
//                     duration: 500,
//                     message: `Un problème est survenu lors de l'ajout, veuillez reessayer`,
//                     position: 'is-bottom-right',
//                     type: 'is-danger',
//                     hasIcon: true
//                 })
//             }
//             else{
//                 this.isLoading = true
//                 this.equipment = []
//                 setTimeout(() => {
//                     this.$store.dispatch('reservations/getReservations');
//                     //location.reload()
//                     this.$el.textContent
//                     this.isLoading = false
//                     this.showReservation = false
//                     this.isComponentModalActive = false
//                     this.$notification.open({
//                         duration: 5000,
//                         message: `Enregistrement effectué avec succès`,
//                         position: 'is-bottom-right',
//                         type: 'is-success',
//                         hasIcon: true
//                     })
//                 }, 500)   
//             }
//         },
//         getReservation(payload){

//             this.reservationOne = this.filterReservations.find(fruit => fruit.id === payload)
//             //console.log(this.equipmentOne)

//             this.reservation.id = this.reservationOne.id
//             this.reservation.start = this.reservationOne.start
//             this.reservation.end = this.reservationOne.end
//             this.reservation.status = this.reservationOne.status
//             this.reservation.motif = this.reservationOne.motif
//             this.reservation.equipment_id = this.reservationOne.equipment_id.id
//             this.reservation.user_id = this.reservationOne.user_id.id
//         },
//         callDelete(id){
//             this.idEqToDel = id
//             this.isDelete = true
//         },
//         deleteReservation(payload){
//             this.$store.dispatch('reservations/deleteReservation', payload)
//             this.isDelete = false
//             this.errors = this.$store.dispatch('reservations/getErrors')
//             //console.log(this.errors)
//             if(this.errors != 400 | this.erros != 500){
//                 setTimeout(() => {
//                     this.$store.dispatch('reservations/getReservations');
//                     //location.reload()
//                     this.$el.textContent
//                     this.isDelete = false
//                     this.isLoading = false
//                     this.showReservation = false
//                     this.isComponentModalActive = false
//                     this.$notification.open({
//                         duration: 5000,
//                         message: `Suppression effectuée avec succès`,
//                         position: 'is-bottom-right',
//                         type: 'is-success',
//                         hasIcon: true
//                     })
//                 }, 500)   
//             }
//             else
//             {
//                 this.$notification.open({
//                     duration: 5000,
//                     message: `Suppression impossible, l'équipement est utilisé par une réservation`,
//                     position: 'is-bottom-right',
//                     type: 'is-danger',
//                     hasIcon: true
//                 })
//             }
//         },
//         updateReservation(payload){
//             //console.log(payload)
//             this.$store.dispatch('reservations/updateReservation', payload)
//             this.errors = this.$store.dispatch('reservations/getErrors')
//             if(this.errors == 400 | this.errors == 500){
//                 this.$notification.open({
//                     duration: 20000,
//                     message: `Un problème est survenu lors de la mise à jour, veuillez reessayer`,
//                     position: 'is-bottom-right',
//                     type: 'is-danger',
//                     hasIcon: true
//                 })
//             }
//             else
//             {
//                 this.isLoading = true
//                 setTimeout(() => {
//                     this.$store.dispatch('reservations/getReservations');
//                     //location.reload()
//                     this.$el.textContent
//                     this.isLoading = false
//                     this.showReservation = false
//                     this.$notification.open({
//                         duration: 5000,
//                         message: `Mise à jour effectuée avec succès`,
//                         position: 'is-bottom-right',
//                         type: 'is-success',
//                         hasIcon: true
//                     })
//                 }, 500)
//             }
//         }
//         ,
//         //Pour la liste déroulante de description
//         toggle(row) {
//             this.$refs.table.toggleDetails(row)
//         },
//     },
//     created() {
//         this.$store.dispatch('reservations/getReservations');
//     }
// }
// </script>
// <style>
// .vl-calendar {
//   display: inline-block;
//   position: relative;
//   background: #f6f6f6;
//   padding: 20px 0 0;
//   text-align: center;
//   color: #3e3a4e;
//   font-size: 14px;
//   user-select: none;
// }
// .vl-calendar__month {
//   display: inline-block;
//   margin-bottom: 30px;
//   width: 300px;
// }
// .vl-calendar__arrow {
//   position: absolute;
//   top: 15px;
//   background-repeat: no-repeat;
//   background-position: center center;
//   background-size: 75%;
//   cursor: pointer;
//   width: 24px;
//   height: 24px;
// }
// .vl-calendar__arrow--back {
//   left: 15px;
//   background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAMAAAAM7l6QAAAA0lBMVEUZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjSTOY05AAAARnRSTlMAAQIDBAUGBwgJCgsMDQ8QERITFBUXGBkaGx0eHyAiIyQnKCkqKywtLi8wMTIzNDU2Nzg5Ojs8Pj9AQUJDREZHSElKS0xNUWPYUAAAAU1JREFUeNptk+lygjAURq8gFm2h1q3uWsVqtZUWXAGtIN/7v1KHSGxYzp9kcnKXJBMSUfRGXZMpl+rcRUS4f6tk5RYINovpdLkPEa7KCVmYhLBbUlyi78DvCrZowmuIuwc+DOJINmyFEjx5mPL5HJZEKVQPHWI04BQpgxZcHlihI6qUwwiLaGjh697iTP/X0ukahZv3YHmLcSJ8SCQFJ243WIstlmET6VjGySxuOa5P1MboZn/Slkyo1EePWRM4eRyL6SU0pm+Fcbmz5TpKztv+oGxyna8qu7R3g+hgHsV+n/QqNkT0jWfuDxgKesgu6RWfFFNa1YRHd0P1NuiUwyC+ryYOctY++r5K8fnMQtqWHPT4W+xgpuLLR8yJo1g4VkXb+YUhJCy8I1zzrqX2Dtdu9huc15Px2LB89g3S1FdnMJyZRrlUaq3mS4kE/gAULzTK6Ml9VwAAAABJRU5ErkJggg==');
// }
// .vl-calendar__arrow--forward {
//   right: 15px;
//   background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAMAAAAM7l6QAAAAz1BMVEUZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjQZJjTQKaQcAAAARXRSTlMAAQIDBAUGBwgJCgsMDg8QERITFBUWGBkaGx0eHyAhIiMkJSYnKCkqLC0uLzAxMjQ1Nzg5Ojs/QEFCQ0RFRkdISUpLTE22Gs8EAAABVUlEQVR4AW3T4XaaMBwF8IvKRp2dU5F266qwMWXT1bWjqbMUanLf/5nWcIzByO9L/udcJRcIaHo3DMeDDlqF64KafIzfwzUVZPWQLZZ3gpSZj6beb6rNxEMtiAu+TGEFgmIIq5sqNYPhC256ODEqeWvme/6C63KvRqh9Ze7hTMRdt65V7vto8ZPf9DLnAtbtzfEZvZYdAEIFsJ44t3+PgIA5GgYvx8pjroArfoeTH67fkQJIeAU3/3LYSAILTvQ43O6MiuoztJzdt3isx09FZezJ2TFOeI0TFztTXkhbrZEmptoTcMEHJzU/H3Gl+6nm4RD8Ycas3jZmCitNzORXZadeXgO0WB52mfEe50L13IPm/eUSrg+VCs2r+8e1c7o/Fozt3Wz5OIDlzSUTWP4fytWlOdU3W1bX55/B812aJFkuqdYBHF60qagpkfbRxutPounQR8N/jIU0mXzMHWoAAAAASUVORK5CYII=');
// }

// .vl-flex {
// 	 display: flex;
// 	 flex-wrap: wrap;
// }
//  .vl-calendar-month {
// 	 padding: 0 20px;
// }
//  .vl-calendar-month__title {
// 	 margin-bottom: 20px;
// 	 text-align: center;
// 	 font-weight: 600;
// }
//  .vl-calendar-month__week-day {
// 	 display: inline-block;
// 	 margin-bottom: 10px;
// 	 width: 14%;
// 	 text-align: center;
// 	 color: #c83f3a;
// 	 font-size: 12px;
// }
//  .vl-calendar-month__day {
// 	 display: inline-flex;
// 	 align-items: center;
// 	 justify-content: center;
// 	 margin: 5px 0;
// 	 cursor: pointer;
// 	 width: 14%;
// 	 height: 24px;
// }
//  .vl-calendar-month__day--offset-1 {
// 	 margin-left: calc(1 * 14%);
// }
//  .vl-calendar-month__day--offset-2 {
// 	 margin-left: calc(2 * 14%);
// }
//  .vl-calendar-month__day--offset-3 {
// 	 margin-left: calc(3 * 14%);
// }
//  .vl-calendar-month__day--offset-4 {
// 	 margin-left: calc(4 * 14%);
// }
//  .vl-calendar-month__day--offset-5 {
// 	 margin-left: calc(5 * 14%);
// }
//  .vl-calendar-month__day--offset-6 {
// 	 margin-left: calc(6 * 14%);
// }
//  .vl-calendar-month__day.disabled {
// 	 color: #b5b5b5;
// 	 pointer-events: none;
// }
//  .vl-calendar-month__day.disabled--first {
// 	 border-top-left-radius: 14px;
// 	 border-bottom-left-radius: 14px;
// }
//  .vl-calendar-month__day.disabled--last {
// 	 border-top-right-radius: 14px;
// 	 border-bottom-right-radius: 14px;
// }
//  .vl-calendar-month__day.selected {
// 	 background: #c83f3a;
// 	 color: #fff;
// 	 font-weight: 800;
// }
//  .vl-calendar-month__day.selected--first {
// 	 border-top-left-radius: 14px;
// 	 border-bottom-left-radius: 14px;
// }
//  .vl-calendar-month__day.selected--last {
// 	 border-top-right-radius: 14px;
// 	 border-bottom-right-radius: 14px;
// }
 


// </style>
