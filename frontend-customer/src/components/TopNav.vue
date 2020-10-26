<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" @click="onRoute('Home')">
      <img src="@/assets/icons/bootstrap.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" @click="onRoute('About')">About</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link" @click="onRoute('Product')">Product</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="onRoute('Event')">Event</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="onRoute('Contact')">Contact</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'TopNav',
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
  }
}
</script>

<style scoped>
.navbar-brand:hover {
  cursor: pointer;
}

.nav-link:hover {
  cursor: pointer;
}

</style>