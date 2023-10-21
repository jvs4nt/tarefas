package br.com.salesforce.beans;

public class Contato {

	
	private String nomeContato;
	private String email;
	private String numeroTelefone;
	private String instagram;
	
	public Contato() {
		super();
	}

	public Contato(String nomeContato, String email, String numeroTelefone, String instagram) {
		super();
		this.nomeContato = nomeContato;
		this.email = email;
		this.numeroTelefone = numeroTelefone;
		this.instagram = instagram;
	}

	public String getNomeContato() {
		return nomeContato;
	}

	public void setNomeContato(String nomeContato) {
		this.nomeContato = nomeContato;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getNumeroTelefone() {
		return numeroTelefone;
	}

	public void setNumeroTelefone(String numeroTelefone) {
		this.numeroTelefone = numeroTelefone;
	}

	public String getInstagram() {
		return instagram;
	}

	public void setInstagram(String instagram) {
		this.instagram = instagram;
	}
	
	
	
}
