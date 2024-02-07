<template>
    <div class="row my-5">
        <div class="col-lg-4" v-for="course in courses" :key="course.id">
            <Card style="overflow: hidden">
                <template #header>
                    <img alt="user header" :src="course.image" />
                </template>
                <template #title>{{ course.name }}</template>
                <template #subtitle>{{ course.category }}</template>
                <template #content>
                    <p class="m-0">
                        {{ course.price }}$
                    </p>
                </template>
                <template #footer>
                    <div class="flex gap-3 mt-1">
                        <Button label="Course Details" class="w-full" />
                    </div>
                </template>
            </Card>


        </div>
    </div>
</template>

<script >

    

    export default {
        name: 'CourseList',
        props: ['courses'],
    }    
</script>

<style >
img{
    
    height: 200px;
}
.p-card{
    margin-top: 10px;
}

</style>