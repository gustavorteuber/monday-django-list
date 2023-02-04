<template>
  <div class="single-date-picker__calendar-month-header">
    <div
      class="single-date-picker__arrow left"
      @click="toggleMonth(-1)"
    >
      <i class="material-icons" >
        <img src="../assets/img/icons8-chevron-esquerda-24.png" alt="">
      </i>
    </div>
    <div class="single-date-picker__year">
      {{ fullMonth }} {{ year }}
    </div>
    <div
      class="single-date-picker__arrow right" 
      @click="toggleMonth(1)"
    >
      <i class="material-icons">
        <img src="../assets/img/icons8-chevron-right-24.png" alt="">
      </i>
    </div>
  </div>
</template>

<script>
const MONTHS = [
  'Janeiro',
  'Fevereiro',
  'Março',
  'Abril',
  'Maio',
  'Junho',
  'Julho',
  'Agosto',
  'Setembro',
  'Outubro',
  'Novembro',
  'Dezembro'
];
export default {
  props: {
    year: {
      type: Number,
      default: () => 1970
    },
    month: {
      type: Number,
      default: () => 0
    }
  },
  computed: {
    fullMonth() {
      return MONTHS[this.month];
    }
  },
  methods: {
    toggleMonth(direction) {
      this.$emit('toggleMonth', direction)
    }
  }
};
</script>

<style lang="scss" scoped>
.single-date-picker__calendar-month-header {
  padding: 15px;
  background-color: #6D28D9;
  display: flex;
  justify-content: space-between;
  border-radius: 10px 10px 0 0;
  align-items: center;
  color: #ffffff;

  .single-date-picker__year {
    font-weight: 900;
    font-size: 20px;
    text-transform: capitalize;
  }
  .single-date-picker__arrow {
    cursor: pointer;
  }
}



</style>