<template>
  <section class="home-section">
    <div class="all">
      <main class="status-page">
        <h1>status</h1>
        <p>This is the status page</p>
      </main>
    </div>
  </section>
</template>
<script>
export default {};
</script>

<style scoped>
.sidebar.open .profile #log_out {
  width: 50px;
  background: none;
}

.home-section {
  position: relative;
  background-color: var(--color-body);
  min-height: 100vh;
  top: 0;
  left: 78px;
  width: calc(100% - 78px);
  transition: all 0.5s ease;
  z-index: 2;
}

.sidebar.open ~ .home-section {
  left: 250px;
  width: calc(100% - 250px);
}
.all {
  display: flex;
}

.status-page {
  width: 100vw;
}
</style>
