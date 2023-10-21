package br.com.salesforce.beans;

public class CampanhaMarketing {

	
	private String nomeCampanha;
	private String dataInicio;
	private String dataFim;
	private double orçamento;
	private String objetivoCampanha;
	
	public CampanhaMarketing() {
		super();
	}

	public CampanhaMarketing(String nomeCampanha, String dataInicio, String dataFim, double orçamento,
			String objetivoCampanha) {
		super();
		this.nomeCampanha = nomeCampanha;
		this.dataInicio = dataInicio;
		this.dataFim = dataFim;
		this.orçamento = orçamento;
		this.objetivoCampanha = objetivoCampanha;
	}

	public String getNomeCampanha() {
		return nomeCampanha;
	}

	public void setNomeCampanha(String nomeCampanha) {
		this.nomeCampanha = nomeCampanha;
	}

	public String getDataInicio() {
		return dataInicio;
	}

	public void setDataInicio(String dataInicio) {
		this.dataInicio = dataInicio;
	}

	public String getDataFim() {
		return dataFim;
	}

	public void setDataFim(String dataFim) {
		this.dataFim = dataFim;
	}

	public double getOrçamento() {
		return orçamento;
	}

	public void setOrçamento(double orçamento) {
		this.orçamento = orçamento;
	}

	public String getObjetivoCampanha() {
		return objetivoCampanha;
	}

	public void setObjetivoCampanha(String objetivoCampanha) {
		this.objetivoCampanha = objetivoCampanha;
	}
	
	
	
}
