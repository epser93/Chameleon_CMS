<template>
  <div class="notice-main">
    <img src="@/assets/250.png" class="notice-img" alt="">
    <!-- <div>
      <div class="notice-btn" id="non-btn" @click="winClose(); winNonOpen();">
        <h5>하루 동안 보지 않기</h5>
      </div>
      <div class="notice-btn" id="close-btn" @click="winClose();">
        <h5>닫기</h5>
      </div>
    </div> -->
    <div class="row mx-0">
      <button class="btn btn-info btn-sm col-6" type="button" @click="winClose(); winNonOpen();">하루 동안 보지 않기</button>
      <button class="btn btn-secondary btn-sm col-6" type="button" @click="winClose();">닫기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Notice',
  data() {
    return {
    }
  },
  methods: {
    // winOpen() {
    //   const event_img = new Image();
    //   event_img.src = this.img_url
    //   const winWidth = event_img.width
    //   const winHeight = this.$refs.notice.clientHeight
    //   this.windowRef = window.open("", "", "innerwidth=" + winWidth + ",innerheight=" + winHeight + ",left=" + (screen.availWidth/2 - winWidth/2) + ",top=" + (screen.availHeight/2 - winHeight/2))
    //   this.windowRef.document.body.appendChild(this.$el)
    //   this.windowRef.document.body.style.margin='auto'
    //   const Btns =  this.windowRef.document.querySelectorAll('.notice-btn')
    //   for ( var i = 0; i < Btns.length; i++ ) { 
    //     Btns[i].style.display = 'inline-block';
    //     Btns[i].style.width = (winWidth/2);
    //     Btns[i].style.textAlign = 'center';
    //   }
    // },
    winClose() {
      window.close()
    },
    winNonOpen() {
      this.$cookies.set('DontOpenNotice','idontwanttoseethat')
    }
  },
}
</script>

<style scoped>
.notice-img {
  width: 100%;
}

</style>