package py.una.pol.sd.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import py.una.pol.sd.model.Recurso;
import java.util.List;

public interface RecursoRepository extends JpaRepository<Recurso, Long> {
    List<Recurso> findByMateria(String materia);
}
