<template>
  <div ref="notice">
    <img :src="img_url" class="notice-img" alt="">
    <div class="notice-btn">
      <h5>하루 동안 보지 않기</h5>
    </div>
    <div class="notice-btn">
      <h5>닫기</h5>
    </div>
  </div>
</template>

<script>
import image from "@/assets/250.png"

export default {
  name: 'Notice',
  data() {
    return {
      img_url: image,
    }
  },
  mounted() {
    const event_img = new Image();
    event_img.src = this.img_url

    const winWidth = event_img.width
    const winHeight = this.$refs.notice.clientHeight
    const windowRef = window.open("", "", "innerwidth=" + winWidth + ",innerheight=" + winHeight + ",left=" + (screen.availWidth/2 - winWidth/2) + ",top=" + (screen.availHeight/2 - winHeight/2))
    windowRef.document.body.appendChild(this.$el)
    windowRef.document.body.style.margin='auto'
    const Btns = windowRef.document.querySelectorAll('.notice-btn')
    for ( var i = 0; i < Btns.length; i++ ) { 
      Btns[i].style.display = 'inline-block';
      Btns[i].style.width = (winWidth/2);
      Btns[i].style.textAlign = 'center';
    }
    windowRef.document.querySelector('.notice-btn :hover').style.backgroundColor='gray'
    console.log(windowRef.document.querySelector('.notice-btn').style)
    // windowRef.close()
  },
}
</script>

<style scoped>
</style>