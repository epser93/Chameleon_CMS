<template>
<div> 미리보기
    <customer-top-nav/>
    {{previewData}}
    <div v-if="previewData">
        들어왓나요?
        <DesignTemplate :data="previewData" v-if="previewData.template == 1"></DesignTemplate>
        <SpecTemplate :data="previewData" v-else-if="previewData.template== 2"></SpecTemplate>
        <CarouselTemplate :data="previewData" v-else-if="previewData.template == 3"></CarouselTemplate>
        <MovingImageTemplate :data="previewData" v-else-if="previewData.template == 4"></MovingImageTemplate>
    </div>
    <Footer/>
</div>
</template>

<script>
import DesignTemplate from '@/customers/Category/DesignTemplate.vue'
import SpecTemplate from '@/customers/Category/SpecTemplate.vue'
import CarouselTemplate from '@/customers/ProductDetail/CarouselTemplate.vue'
import MovingImageTemplate from '@/customers/ProductDetail/MovingImageTemplate.vue'
import CustomerTopNav from '@/components/CustomerTopNav'
import Footer from '@/components/Footer'

export default {
    data(){
        return {    
            previewData: '',
        }
    },
    components: {
        DesignTemplate,
        SpecTemplate,
        CarouselTemplate,
        MovingImageTemplate,
        CustomerTopNav,
        Footer,
    },
    created() {
        this.previewData = JSON.parse(window.opener.document.myform.sender.value)
    }
}
</script>

<style>

</style>