<template>
  <div @mouseleave="onHideWide()">
    <nav class="navbar fixed-top navbar-expand-md navbar-light bg-light">
      
      <!-- logo -->
      <a class="navbar-brand" @click="onRoute('CustomerHome'); onHideWide(); onHideCollapse();" >
        <img src="@/assets/logo.png" width="100" height="42" class="d-inline-block align-top" alt="" loading="lazy">
      </a>

      <!-- searchbar -->
      <a class="nav-item ml-auto mr-4 d-md-none" @click="onHideCollapse();" data-toggle="collapse" data-target="#searchBar" aria-controls="searchBar" aria-expanded="false">
        <img src="@/assets/icons/search.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
      </a>

      <button class="navbar-toggler" @click="onHideProduct(); onHideSearch();" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- topbar -->
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onRoute('CustomerAbout'); onHideWide(); onHideCollapse();">About</a>
          </li>
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onHideSearch()" data-toggle="collapse" data-target=".productContent" aria-controls="productContent" aria-expanded="false">Product</a>
          </li>
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onRoute('CustomerEvent'); onHideWide(); onHideCollapse();">Event</a>
          </li>
          <li class="nav-item mx-4">
            <a class="nav-link" @click="onRoute('CustomerContact'); onHideWide(); onHideCollapse();">Contact</a>
          </li>
        </ul>
      </div>

      <!-- searchbar 누르면 나오는 section-->
      <a class="nav-item ml-auto mr-4 d-none d-md-block" @click="onHideWide();" data-toggle="collapse" data-target="#searchBar" aria-controls="searchBar" aria-expanded="false">
        <img src="@/assets/icons/search.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
      </a>
    </nav>

    <!-- product dropdown -->
    <div class="d-none d-md-block" id="dropDown">
      <div class="collapse bg-light productContent" id="productWide">
        <div class="row mx-4 pt-2 pb-4 float-top">
          <div class="nav nav-pills flex-column col-2 bg-light" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a v-for="(category, index) in categories" :key="index" :class="(index===0) ? 'nav-link active' : 'nav-link'" :id="`v-pills-${category.name}-tab`" data-toggle="tab" :href="`#v-pills-${category.name}`" role="tab" :aria-controls="`v-pills-${category.name}`" :aria-selected="true">{{ category.name }} </a>
          </div>
            <div class="tab-content col-10 bg-light" id="v-pills-tabContent">
              <div v-for="(category, index) in categories" :key="index" :class="index === 0 ? 'tab-pane fade show active' : 'tab-pane fade'" :id="`v-pills-${category.name}`" role="tabpanel" :aria-labelledby="`v-pills-${category.name}-tab`">
                <div class="card card-body">
                  <div class="row">
                    <div class="nav nav-pills col-3 flex-column" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                      <a :class="(index === 0) ? 'nav-link active' : 'nav-link'" v-for="(item, index) in category.items" :key="index" @click="onRoute('CarouselTemplate')" data-toggle="tab"  role="tab" :aria-selected="(index) ? true : false">{{ item.name }}</a>
                      <a class="nav-link" @click="onDetail(category.id); onHideWide();" data-toggle="tab" role="tab" aria-selected="false">더 알아보기</a>
                    </div>
                    <div class="col-9">
                      <img class="category-thumbanil" :src="getImage(category.image)" alt="dummy">
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
        <input v-model="search" @keypress.enter="onSearch(); onHideSearch()" type="text" class="form-control" placeholder="Search Content" aria-label="Recipient's username" aria-describedby="basic-addon2">
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" @click="onSearch(); onHideSearch();">Search</button>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import $ from 'jquery'
import SERVER from '@/api/drf'
import axios from 'axios'
export default {
  name: 'CustomerTopNav',
  data() {
    return {
      categories: '',
      search: '',
    }
  },
  methods: {
    onRoute(name) {
      this.$router.push({name: name}, () => {})
    },
    onDetail(cid) {
      this.$router.push({name: 'CustomerCategory', params:{ cid: cid }}, () => {})
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
      if (this.search == '') {
        alert('검색어가 없습니다.')
      } else {
        this.$router.push({name:'CustomerSearch', params:{text: this.search}}, () => {})
        this.search = ''
      }
    },
    getNavInfo() {
      axios.get(SERVER.URL + SERVER.ROUTER.customer.category)
        .then(res => {
          this.categories = res.data
        })
        .catch(error => console.log(error.response))
    },
    getImage(src) {
      if (src) {
        return SERVER.domain + src.slice(56, src.length)
      }
      return ''
    }
  },
  created() {
    this.getNavInfo()
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

#dropDown {
  position: absolute;
  z-index: 999999;
  width: 100vw;
  margin-top: -18px;
}

#searchBar {
  position: absolute;
  width: 100vw;
  z-index: 999999;
  margin-top: -18px;
}

.nav-link {
  position: relative;
  font-size: 1.3rem;
  font-family: 'Raleway', sans-serif;
  cursor: pointer;
}

#navbarSupportedContent {
  font-family: 'Raleway', sans-serif;
}

#v-pills-home-tab {
  font-family: 'Raleway', sans-serif;
}
</style>