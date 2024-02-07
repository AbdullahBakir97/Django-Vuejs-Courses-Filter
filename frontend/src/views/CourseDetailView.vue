<template>
    <div class="container my-5">
        <div class="row">
            <div class="col-lg-6">
                <img :src="course.image" class="img-fluid" alt="">
            </div>
            <div class="col-lg-6">
                <h3 class="card-title">{{ course.name }}</h3>
                <p class="card-text">{{ course.category }}</p>
                <p class="card-text">{{ course.price }}$</p>
                <form class="row">
                    <div class="col-lg-6">
                        <input type="number" value="1" class="form-control">
                    </div>
                    <div class="col-lg-6">
                        <button class="btn btn-info"> Add To Cart </button>
                    </div>
                </form>
            </div>
        </div>/
        
    </div>
</template>

    
<script >
    import { courses } from '../temp-data'

    export default {
        name: 'CourseDetail',
        data() {
            return {
                course: courses.find( course => course.id == this.$route.params.courseId )
            }
        }

    } 
</script>
