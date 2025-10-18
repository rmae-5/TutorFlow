package py.una.pol.sd.service;

import org.springframework.stereotype.Service;
import py.una.pol.sd.model.Recurso;
import py.una.pol.sd.repository.RecursoRepository;
import java.util.List;

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
}
