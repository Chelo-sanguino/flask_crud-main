// Componente para cada fila de artículo
const ArticuloComponent = {
  props: ['articulo'],
  template: `
    <tr>
      <td>{{ articulo.id }}</td>
      <td>{{ articulo.codigo }}</td>
      <td>{{ articulo.nombre }}</td>
      <td>{{ articulo.precio }}</td>
      <td class="text-center">
        <div class="d-flex justify-content-center gap-2">
          <button @click="$emit('editar', articulo)" class="button editar" data-text="Editar">
            <span class="actual-text">&nbsp;Editar&nbsp;</span>
            <span class="hover-text">&nbsp;Editar&nbsp;</span>
          </button>
          <button @click="$emit('eliminar', articulo.id)" class="button eliminar" data-text="Eliminar">
            <span class="actual-text">&nbsp;Eliminar&nbsp;</span>
            <span class="hover-text">&nbsp;Eliminar&nbsp;</span>
          </button>
        </div>
      </td>
    </tr>
  `
};

// Verificar que Vue está disponible
if (typeof Vue === 'undefined') {
  console.error('Vue no está cargado');
} else {
  console.log('Vue versión:', Vue.version);
  
  // Crear la aplicación Vue
  const app = Vue.createApp({
    components: {
      ArticuloComponent
    },
    data() {
      return {
        articulos: [],
        cargando: true,
        error: null
      };
    },
    methods: {
      async fetchArticulos() {
        try {
          console.log('Iniciando fetchArticulos...');
          this.cargando = true;
          
          const response = await fetch('/api/articulos/');
          console.log('Response status:', response.status);
          
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          
          const data = await response.json();
          console.log('Datos recibidos:', data);
          
          if (Array.isArray(data)) {
            this.articulos = data;
            console.log('Artículos cargados:', this.articulos.length);
          } else {
            throw new Error('Los datos recibidos no son un array');
          }
        } catch (error) {
          console.error('Error en fetchArticulos:', error);
          this.error = error.message;
        } finally {
          this.cargando = false;
        }
      },
      editarArticulo(articulo) {
        window.location.href = `/articulos/edit/${articulo.id}`;
      },
      async eliminarArticulo(id) {
        if (!confirm('¿Está seguro de que desea eliminar este artículo?')) return;
        
        try {
          const response = await fetch(`/api/articulos/${id}`, {
            method: 'DELETE',
          });
          
          if (!response.ok) {
            throw new Error('Error al eliminar el artículo');
          }
          
          await this.fetchArticulos();
          alert('Artículo eliminado exitosamente');
        } catch (error) {
          console.error('Error al eliminar:', error);
          alert('Error al eliminar el artículo');
        }
      }
    },
    mounted() {
      console.log('Componente montado');
      this.fetchArticulos();
    }
  });

  // Asegurarse de que el elemento #app existe antes de montar
  const appElement = document.getElementById('app');
  if (appElement) {
    console.log('Montando aplicación Vue en #app');
    app.mount('#app');
  } else {
    console.error('No se encontró el elemento #app');
  }
}