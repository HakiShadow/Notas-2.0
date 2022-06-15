package com.baufest.tennis.springtennis.model;

import com.baufest.tennis.springtennis.enums.Estado;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name="partido")
public class Partido {

    @Id
    @GeneratedValue (strategy = GenerationType.IDENTITY)
    private long id;

    @Column(nullable = false)
    private Date fechaComienzo;

    @Column(nullable = false)
    private Estado estado;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "idLocal", nullable=false)
    private Jugador jugadorLocal;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "idVisitante", nullable=false)
    private Jugador jugadorVisitante;

    @Column(nullable = false)
    private int scoreLocal;

    @Column(nullable = false)
    private String puntosGameActualidad;

    @Column(nullable = false)
    private int cantidadGamesLocal;

    @Column(nullable = false)
    private int scoreVisitante;

    @Column(nullable = false)
    private String puntosGameActualVisitante;

    @Column(nullable = false)
    private int cantidadGamesVisitante;


    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public Date getFechaComienzo() {
        return fechaComienzo;
    }

    public void setFechaComienzo(Date fechaComienzo) {
        this.fechaComienzo = fechaComienzo;
    }

    public Estado getEstado() {
        return estado;
    }

    public void setEstado(Estado estado) {
        this.estado = estado;
    }

    public Jugador getJugadorLocal() {
        return jugadorLocal;
    }

    public void setJugadorLocal(Jugador jugadorLocal) {
        this.jugadorLocal = jugadorLocal;
    }

    public Jugador getJugadorVisitante() {
        return jugadorVisitante;
    }

    public void setJugadorVisitante(Jugador jugadorVisitante) {
        this.jugadorVisitante = jugadorVisitante;
    }

    public int getScoreLocal() {
        return scoreLocal;
    }

    public void setScoreLocal(int scoreLocal) {
        this.scoreLocal = scoreLocal;
    }

    public String getPuntosGameActualidad() {
        return puntosGameActualidad;
    }

    public void setPuntosGameActualidad(String puntosGameActualidad) {
        this.puntosGameActualidad = puntosGameActualidad;
    }

    public int getCandidadGamesLocal() {
        return cantidadGamesLocal;
    }

    public void setCandidadGamesLocal(int candidadGamesLocal) {
        this.cantidadGamesLocal = candidadGamesLocal;
    }

    public int getScoreVisitante() {
        return scoreVisitante;
    }

    public void setScoreVisitante(int scoreVisitante) {
        this.scoreVisitante = scoreVisitante;
    }

    public String getPuntosGameActualVisitante() {
        return puntosGameActualVisitante;
    }

    public void setPuntosGameActualVisitante(String puntosGameActualVisitante) {
        this.puntosGameActualVisitante = puntosGameActualVisitante;
    }

    public int getCantidadGamesVisitante() {
        return cantidadGamesVisitante;
    }

    public void setCantidadGamesVisitante(int cantidadGamesVisitante) {
        this.cantidadGamesVisitante = cantidadGamesVisitante;
    }
}
