<template>
<section class="hero is-medium is-primary is-bold">
  <div class="hero-body">
    <div class="container">
      <h1 class="title">
        Quelques statistiques
      </h1>
      <div class="container">
      <hr>
        <div class="tile is-ancestor">
          <div class="tile is-parent">
            <article class="tile is-child box notification is-success">
              <p class="title">Total des équipements</p>
              <div class="content">
                <h1 class="title is-1">{{equipments.length}}</h1>
              </div>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-info">
              <p class="title">Equipements réservés</p>
              <div class="content">
                <h1 class="title is-2">{{reservationOk.length}}</h1>
                <em v-if="reservationNok.length">Non réservés : {{reservationNok.length}}</em>
              </div>
              <figure class="image is-6by3">
              </figure>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child box notification is-primary">
              <p class="title">Membres du personnel</p>
              <div class="content">
                <h1 class="title is-1">{{users.length}}</h1>
              </div>
            </article>
          </div>
        </div>
      </div>
      <br>
      <h1 class="title">
        Quelques lignes sur le support
      </h1>
      <div>
        <hr>
        <b-message type="is-info" has-icon>
            Aucune information pour le moment.
        </b-message>
      </div>
    </div>
  </div>
</section>
</template>

<script>
export default {
  computed:{
    reservations(){
      return this.$store.state.reservations.reservations
    },

    reservationOk(){
      return this.$store.state.reservations.reservations.filter((key)=>{
          if(key.status)
          return key.status.match("0")
      })
    },
    reservationNok(){
      return this.$store.state.reservations.reservations.filter((key)=>{
          if(key.status)
          return key.status.match("1")
      })
    },

    equipments(){
      return this.$store.state.equipments.equipments
    },

    users(){
      return this.$store.getters['authentication/users']
    },
  },
  created(){
    this.$store.dispatch('authentication/getUsers')
    this.$store.dispatch('authentication/getUser')
  }
}
</script>