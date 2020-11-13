<template>

<div> 미리보기
    {{ datas }}
    {{ data }}
    {{previewData}}
    <div v-if="previewData">
        들어왓나요?
        <DesignTemplate :data="previewData" v-if="previewData.template == 1">rrrr</DesignTemplate>
        <SpecTemplate :data="previewData" v-else-if="previewData.template== 2">ss</SpecTemplate>
        <CarouselTemplate :data="previewData" v-else-if="previewData.template == 3">aa</CarouselTemplate>
        <MovingImageTemplate :data="previewData" v-else-if="previewData.template == 4">ff</MovingImageTemplate>
    </div>
</div>
</template>

<script>
import DesignTemplate from '@/customers/Category/DesignTemplate.vue'
import SpecTemplate from '@/customers/Category/SpecTemplate.vue'
import CarouselTemplate from '@/customers/ProductDetail/CarouselTemplate.vue'
import MovingImageTemplate from '@/customers/ProductDetail/MovingImageTemplate.vue'
import { mapState } from 'vuex'

export default {
    data(){
        return {
            datas: ''
        }
    },
    components: {
        DesignTemplate,
        SpecTemplate,
        CarouselTemplate,
        MovingImageTemplate
    },
    computed: {
        ...mapState('category', ['previewData'])
        
    },
    created(){
        // get_element;
        // console.log(get_elements())
        // window.addEventListener("message", ({data}) => {
        //     window.postMessage("received","*");
        //     this.data = data
        //     console.log(data)
      //Do whatever with data
        // });
        
        // opener.document.all.previewData.value = this.datas;
        // console.log(window.opener.document)
    }
}
</script>

<style>

</style>