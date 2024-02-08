<template>
  <h3> Courses Filter </h3>
  <form class="card">
    
    <div class="flex align-items-center checkbox" v-for="cat in category" :key="cat.id">
      <Checkbox v-model="selectedCategory" :inputId="cat.id" :name="cat.name" :value="cat.id" />
      <label :for="cat.id" class="ml-2"> {{cat.name}} </label>
    </div>
    
  </form>
  
</template>

<script >
import axios from 'axios'
  export default {
    name: 'CourseFilter',
    data () {
      return {
        category: [],
        selectedCategory: []
      }
    },
    watch:{
      selectedCategory(){
        this.$emit('filter', this.selectedCategory)
      },
    },
    created(){
      this.getCategory()
    },
    methods: {
        getCategory(){
          axios.get("http://127.0.0.1:8000/api/category")
          .then(response => {
            this.category = response.data
          })
        },
    }
  }    
</script>

<style>

.checkbox{
  margin:10px
}

</style>