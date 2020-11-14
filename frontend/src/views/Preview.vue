<template>
<div v-if="previewData"> 
    <!-- customer-top-nav -->
    <div @mouseleave="onHideWide()">
    <nav class="navbar fixed-top navbar-expand-md navbar-light bg-light">
    
    <!-- logo -->
    <a class="navbar-brand">
        <img src="@/assets/logo.png" width="100" height="42" class="d-inline-block align-top" alt="">
    </a>

    <!-- searchbar -->
    <a class="nav-item ml-auto mr-4 d-md-none" data-toggle="collapse" data-target="#searchBar" aria-controls="searchBar" aria-expanded="false">
        <img src="@/assets/icons/search.svg" width="30" height="30" class="d-inline-block align-top" alt="">
    </a>

    <button class="navbar-toggler" @click="onHideSearch();" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <!-- topbar -->
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mx-auto">
        <li class="nav-item mx-4">
            <a class="nav-link">About</a>
        </li>
        <li class="nav-item mx-4">
            <a class="nav-link" @click="onHideSearch()" data-toggle="collapse" data-target=".productContent" aria-controls="productContent" aria-expanded="false">Product</a>
        </li>
        <li class="nav-item mx-4">
            <a class="nav-link">Event</a>
        </li>
        <li class="nav-item mx-4">
            <a class="nav-link">Contact</a>
        </li>
        </ul>
    </div>

    <!-- searchbar 누르면 나오는 section-->
      <a class="nav-item ml-auto mr-4 d-none d-md-block" data-toggle="collapse" data-target="#searchBar" aria-controls="searchBar" aria-expanded="false">
        <img src="@/assets/icons/search.svg" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
      </a>
    </nav>

    <!-- product dropdown -->
    <div class="d-none d-md-block" id="dropDown">
      <div class="collapse bg-light productContent" id="productWide">
        <div class="row mx-4 pt-2 pb-4 float-top">
          <div class="nav nav-pills flex-column col-2 bg-light" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a class="nav-link active" :id="`v-pills-${previewData.name}-tab`" data-toggle="tab" :href="`#v-pills-${previewData.name}`" role="tab" :aria-controls="`v-pills-${previewData.name}`" :aria-selected="true">{{ previewData.name }} </a>
          </div>
            <div class="tab-content col-10 bg-light" id="v-pills-tabContent">
              <div class="tab-pane fade show active" :id="`v-pills-${previewData.name}`" role="tabpanel" :aria-labelledby="`v-pills-${previewData.name}-tab`">
                <div class="card card-body">
                  <div class="row">
                    <div class="nav nav-pills col-3 flex-column" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                      <a class="nav-link" v-for="(item, index) in previewData.items" :key="index" data-toggle="tab" role="tab" :aria-selected="(index) ? true : false">{{ item.name }}</a>
                      <a class="nav-link" @click="onHideWide();" data-toggle="tab" role="tab" aria-selected="false">더 알아보기</a>
                    </div>
                    <div class="col-9">
                      <img class="category-thumbanil" :src="(previewData.image)" alt="dummy">
                    </div>
                  </div>
                </div>
              </div>
            </div>  
        </div>
      </div>
    </div>
  </div>
    <!-- {{ previewData.items[0] }} -->
    {{ this.thumbImg }}
    {{ previewData.template}}
    <!-- 내용 -->
    <div v-if="previewData">
        <SpecTemplate :datas="previewData" v-if="previewData.template== 1"></SpecTemplate>
        <DesignTemplate :datas="previewData" v-else-if="previewData.template == 2"></DesignTemplate>
        <CarouselTemplate :checkPoint="previewData.template" :itemInfo="previewData.items[0]" :previewThumbnails ="this.thumbImg" :previewDetails ="this.detailImg" v-else-if="previewData.items[0].template == 3"></CarouselTemplate>
        <MovingImageTemplate :checkPoint="previewData.template" :itemInfo="previewData.items[0]" :previewThumbnails ="this.thumbImg" :previewDetails ="this.detailImg" v-else-if="previewData.items[0].template == 4"></MovingImageTemplate>
    </div>

  <!-- Site footer -->
    <footer class="site-footer">
      <div class="container">
        <div class="row justify-content-between">
          <div class="col-sm-12 col-md-6">
            <h6>About</h6>
            <p class="text-justify">Web CMS Solution, Chamaeleon</p>
          </div>
          <div class="col-xs-6 col-md-3">
            <h6>Categories</h6>
            <ul class="footer-links">
              <li>About</li>
              <li>Product</li>
              <li>Event</li>
              <li>Contact</li>
            </ul>
          </div>
        </div>
        <hr>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-8 col-sm-6 col-xs-12">
            <p class="copyright-text">Copyright &copy; 2020 All Rights Reserved by 
         <a href="#">Chmaeleon</a>.
            </p>
          </div>
        </div>
      </div>
    </footer>

</div>
</template>

<script>
import $ from 'jquery'
import DesignTemplate from '@/customers/Category/DesignTemplate.vue'
import SpecTemplate from '@/customers/Category/SpecTemplate.vue'
import CarouselTemplate from '@/customers/ProductDetail/CarouselTemplate.vue'
import MovingImageTemplate from '@/customers/ProductDetail/MovingImageTemplate.vue'

export default {
    data(){
        return {    
            previewData: '',
            thumbImg: [],
            detailImg: [],
        }
    },
    components: {
        DesignTemplate,
        SpecTemplate,
        CarouselTemplate,
        MovingImageTemplate,
    },
    methods: {
        onHideCollapse() {
        $('.collapse').collapse('hide')
        },
        onHideWide() {
        $('#productWide').collapse('hide')
        },
        onHideSearch() {
        $('#searchBar').collapse('hide')
        },
        divideImg() {
            const tmpImgLen = this.previewData.items[0].images.length
            for(let i=0; i<tmpImgLen; i++){
                
                if(this.previewData.items[0].images[i].is_thumbnail == true) {
                    const thumbnails = {
                        "item_image" : this.previewData.items[0].images[i].item_image 
                    }
                    this.thumbImg.push(thumbnails)
                } else {
                    const thumbnails = {
                        "item_image" : this.previewData.items[0].images[i].item_image 
                    }
                    this.detailImg.push(thumbnails)
                }
            }
        }
    },
    created() {
        this.previewData = JSON.parse(window.opener.document.myform.sender.value)
        this.divideImg()
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



.site-footer
{
  background-color:#26272b;
  padding:45px 0 20px;
  font-size:15px;
  line-height:24px;
  color:#737373;
  bottom: 0;
}
.site-footer hr
{
  border-top-color:#bbb;
  opacity:0.5
}
.site-footer hr.small
{
  margin:20px 0
}
.site-footer h6
{
  color:#fff;
  font-size:16px;
  text-transform:uppercase;
  margin-top:5px;
  letter-spacing:2px
}
.site-footer a
{
  color:#737373;
}
.site-footer a:hover
{
  color:#3366cc;
  text-decoration:none;
}
.footer-links
{
  padding-left:0;
  list-style:none
}
.footer-links li
{
  display:block
}
.footer-links a
{
  color:#737373
}
.footer-links a:active,.footer-links a:focus,.footer-links a:hover
{
  color:#3366cc;
  text-decoration:none;
}
.footer-links.inline li
{
  display:inline-block
}
.site-footer .social-icons
{
  text-align:right
}
.site-footer .social-icons a
{
  width:40px;
  height:40px;
  line-height:40px;
  margin-left:6px;
  margin-right:0;
  border-radius:100%;
  background-color:#33353d
}
</style>