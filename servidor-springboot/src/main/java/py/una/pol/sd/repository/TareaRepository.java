package py.una.pol.sd.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import py.una.pol.sd.model.Tarea;

public interface TareaRepository extends JpaRepository<Tarea, Long> {
    //agregar metodos
}
