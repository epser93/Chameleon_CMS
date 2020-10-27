<template>
  <div class="fixed-top" @mouseleave="onHideWide()">
    <nav class="navbar navbar-expand-md navbar-light bg-light">
      
      <a class="navbar-brand" @click="onRoute('Home'); onHideWide(); onHideCollapse();" >
        <img src="@/assets/icons/bootstrap.svg" width="42" height="42" class="d-inline-block align-top" alt="" loading="lazy">
      </a>

      <a class="nav-item ml-auto mr-4 d-md-none" @click="onHideCollapse();" data-toggle="collapse" data-target="#searchBar" aria-controls="searchBar" aria-expanded="false">
        <img src="@/assets/icons/search.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
      </a>

      <button class="navbar-toggler" @click="onHideProduct(); onHideSearch();" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onRoute('About'); onHideWide(); onHideCollapse();">About</a>
          </li>
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onHideSearch()" data-toggle="collapse" data-target=".productContent" aria-controls="productContent" aria-expanded="false"  >Product</a>
            <div class="collapse d-md-none productContent" id="productToggle">
              <div class="card card-body">
                <div class="nav nav-pills flex-column" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                  <a class="nav-link active" @click="onRoute('DesignTemplate'); onHideCollapse();" data-toggle="tab"  role="tab" aria-selected="true">DesignTemplate</a>
                  <a class="nav-link" @click="onRoute('SpecTemplate'); onHideCollapse();" data-toggle="tab" role="tab" aria-selected="false">SpecTemplate</a>
                  <a class="nav-link" data-toggle="tab" role="tab" aria-selected="false">categoryC</a>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onRoute('Event'); onHideWide(); onHideCollapse();">Event</a>
          </li>
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onRoute('Contact'); onHideWide(); onHideCollapse();">Contact</a>
          </li>
        </ul>
      </div>

      <a class="nav-item ml-auto mr-4 d-none d-md-block" @click="onHideWide();" data-toggle="collapse" data-target="#searchBar" aria-controls="searchBar" aria-expanded="false">
        <img src="@/assets/icons/search.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
      </a>
      
    </nav>

    <div class="d-none d-md-block">
      <div class="collapse bg-light productContent" id="productWide">
        <div class="row mx-4 pt-2 pb-4">
          <div class="nav nav-pills flex-column col-2 bg-light" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a class="nav-link active" id="v-pills-home-tab" data-toggle="tab" href="#v-pills-home" role="tab" aria-controls="v-pills-home" aria-selected="true">DesignTemplate</a>
            <a class="nav-link" id="v-pills-profile-tab" data-toggle="tab" href="#v-pills-profile" role="tab" aria-controls="v-pills-profile" aria-selected="false">SpecTemplate</a>
            <a class="nav-link" id="v-pills-messages-tab" data-toggle="tab" href="#v-pills-messages" role="tab" aria-controls="v-pills-messages" aria-selected="false">categoryC</a>
          </div>
          <div class="tab-content col-10 bg-light" id="v-pills-tabContent">
            <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">
              <div class="card card-body">
                <div class="row">
                  <div class="nav nav-pills col-3 flex-column" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                    <a class="nav-link active" data-toggle="tab"  role="tab" aria-selected="true">itemA</a>
                    <a class="nav-link" data-toggle="tab" role="tab" aria-selected="false">itemB</a>
                    <a class="nav-link" data-toggle="tab" role="tab" aria-selected="false">itemC</a>
                    <a class="nav-link" @click="onRoute('DesignTemplate'); onHideWide();" data-toggle="tab" role="tab" aria-selected="false">더 알아보기</a>
                  </div>
                  <div class="col-9">
                    <img class="category-thumbanil" src="https://picsum.photos/500/500" alt="dummy">
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab">
              <div class="card card-body">
                <div class="row">
                  <div class="nav nav-pills col-3 flex-column" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                    <a class="nav-link active" data-toggle="tab"  role="tab" aria-selected="true">itemA</a>
                    <a class="nav-link" data-toggle="tab" role="tab" aria-selected="false">itemB</a>
                    <a class="nav-link" @click="onRoute('SpecTemplate'); onHideWide();" data-toggle="tab" role="tab" aria-selected="false">더 알아보기</a>
                  </div>
                  <div class="col-9">
                    <img class="category-thumbanil" src="https://picsum.photos/500/500" alt="dummy">
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade" id="v-pills-messages" role="tabpanel" aria-labelledby="v-pills-messages-tab">
              <div class="card card-body">
                <div class="row">
                  <div class="nav nav-pills col-3 flex-column" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                    <a class="nav-link active" data-toggle="tab"  role="tab" aria-selected="true">itemA</a>
                    <a class="nav-link" data-toggle="tab" role="tab" aria-selected="false">itemB</a>
                    <a class="nav-link" data-toggle="tab" role="tab" aria-selected="false">itemC</a>
                  </div>
                  <div class="col-9">
                    <img class="category-thumbanil" src="https://picsum.photos/500/500" alt="dummy">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    
    <div class="collapse bg-light" id="searchBar">
      <div class="input-group pt-2 pb-4 mx-auto" id="searchContent">
        <input v-model="search" type="text" class="form-control" placeholder="Search Content" aria-label="Recipient's username" aria-describedby="basic-addon2">
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" @click="onSearch(); onHideSearch();">Search</button>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'TopNav',
  data() {
    return {
      search: ''
    }
  },
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
    onHideCollapse() {
      $('.collapse').collapse('hide')
    },
    onHideProduct() {
      $('.productContent').collapse('hide')
    },
    onHideWide() {
      $('#productWide').collapse('hide')
    },
    onHideSearch() {
      $('#searchBar').collapse('hide')
    },
    onSearch() {
      this.$router.push({name:'Search', params:{text: this.search}})
      this.search = ''
		},
  }
}
</script>

<style scoped>
.navbar {
  min-height: 68px;
}

.navbar-brand:hover {
  cursor: pointer;
}

.nav-link {
  font-size: 24px;
}

.nav-item:hover {
  cursor: pointer;
}

.nav-pills .nav-link.active {
  background-color: gray!important;
  color: #f8f9fa!important;
}

.nav-pills .nav-link {
  color: rgba(0,0,0,.5)!important;
}

#searchContent {
  width: 80%;
}

.category-thumbnail {
  width: 100%;
}

</style>