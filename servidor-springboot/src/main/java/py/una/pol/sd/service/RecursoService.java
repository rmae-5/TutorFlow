package py.una.pol.sd.service;

import org.springframework.stereotype.Service;
import py.una.pol.sd.model.Recurso;
import py.una.pol.sd.repository.RecursoRepository;
import java.util.List;
import java.util.Optional;

@Service
public class RecursoService {
    private final RecursoRepository repo;

    public RecursoService(RecursoRepository repo) {
        this.repo = repo;
    }

    public List<Recurso> listarTodos() {
        return repo.findAll();
    }

    public List<Recurso> porMateria(String materia) {
        return repo.findByMateria(materia);
    }

    public Recurso guardar(Recurso recurso) {
        return repo.save(recurso);
    }

    public Optional<Recurso> actualizar(Long id, Recurso recursoActualizado) {
        return repo.findById(id).map(recurso -> {
            recurso.setTitulo(recursoActualizado.getTitulo());
            recurso.setDescripcion(recursoActualizado.getDescripcion());
            recurso.setMateria(recursoActualizado.getMateria());
            return repo.save(recurso);
        });
    }

    public void eliminar(Long id) {
        repo.deleteById(id);
    }
}
