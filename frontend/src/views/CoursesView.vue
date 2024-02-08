<template>
    <div class="container my-5">
        <div class="row">
            <div class="col-lg-3"><CourseFilter @filter="filtercourses"/></div>
            <div class="col-lg-9"><CourseList :courses="filteredCourses" /></div>
        </div>
    </div>

</template>


<script >
    import CourseList from '@/components/CourseList.vue'
    import CourseFilter from '@/components/CourseFilter.vue'

    import axios from 'axios'

    export default {
        name: 'CoursesView',
        
        components: {
            CourseList,
            CourseFilter,
        },
        data(){
            return {
                courses:[],
                filteredCourses:[]
            }
        },
        created(){
            this.getCourses()
        },

        methods: {

            getCourses(){
                axios.get('http://localhost:8000/api/courses')
                .then(response => {
                    this.courses = response.data
                    this.filteredCourses = response.data
                })
            },

            async filtercourses(selectedCategory){
                if (selectedCategory.length == 0){
                    this.filteredCourses = this.courses
                }
                else{
                    this.filteredCourses = this.courses.filter(course => selectedCategory.includes(course.category_id ))
                    
                    console.log(selectedCategory)
                    const categoryIDS = selectedCategory.join(',')
                    const response =  await axios.get(`http://localhost:8000/api/courses?category=${categoryIDS}`)
                    this.filteredCourses = response.data

                }

                
            }
        }
        
    }    
</script>
