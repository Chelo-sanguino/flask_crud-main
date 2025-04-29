const ArticuloComponent = {
  props: ['articulo'],
  template: `
    <tr>
      <td :title="articulo.id">{{ articulo.id }}</td>
      <td :title="articulo.codigo">{{ articulo.codigo }}</td>
      <td :title="articulo.nombre">{{ articulo.nombre }}</td>
      <td :title="articulo.precio">{{ articulo.precio }}</td>
      <td>
        <div class="d-flex justify-content-center gap-2">
          <button @click="$emit('editar', articulo)" class="button editar" data-text="Editar">
            <span class="actual-text">&nbsp;Editar&nbsp;</span>
            <span aria-hidden="true" class="hover-text">&nbsp;Editar&nbsp;</span>
          </button>
          <button @click="$emit('eliminar', articulo.id)" class="button eliminar" data-text="Eliminar">
            <span class="actual-text">&nbsp;Eliminar&nbsp;</span>
            <span aria-hidden="true" class="hover-text">&nbsp;Eliminar&nbsp;</span>
          </button>
        </div>
      </td>
    </tr>
  `
};

const app = Vue.createApp({
  components: {
    ArticuloComponent
  },
  data() {
    return {
      articulos: []
    };
  },
  methods: {
    fetchArticulos() {
      fetch('/api/articulos/')
        .then(response => {
          if (!response.ok) {
            throw new Error('Error al obtener los artículos');
          }
          return response.json();
        })
        .then(data => {
          this.articulos = data;
        })
        .catch(error => {
          console.error('Error:', error);
        });
    },
    editarArticulo(articulo) {
      // Redirigir a la página de edición
      window.location.href = `/articulos/edit/${articulo.id}`;
    },
    eliminarArticulo(id) {
      if (confirm('¿Está seguro de que desea eliminar este artículo?')) {
        fetch(`/api/articulos/${id}`, {
          method: 'DELETE',
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Error al eliminar el artículo');
          }
          return response.json();
        })
        .then(data => {
          // Actualizar la lista de artículos después de eliminar
          this.fetchArticulos();
          // Mostrar mensaje de éxito
          alert('Artículo eliminado exitosamente');
        })
        .catch(error => {
          console.error('Error:', error);
          alert('Error al eliminar el artículo');
        });
      }
    }
  },
  mounted() {
    this.fetchArticulos();
  }
});

app.mount('#app');