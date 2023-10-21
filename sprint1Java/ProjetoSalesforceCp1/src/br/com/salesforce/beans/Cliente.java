package br.com.salesforce.beans;

public class Cliente {

	
	private String nome;
	private String empresa;
	private String dtCadastro;
	private Endereco endereco;
	private Contato contato;
	
	public Cliente() {
		super();
	}

	public Cliente(String nome, String empresa, String dtCadastro) {
		super();
		this.nome = nome;
		this.empresa = empresa;
		this.dtCadastro = dtCadastro;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getEmpresa() {
		return empresa;
	}

	public void setEmpresa(String empresa) {
		this.empresa = empresa;
	}

	public String getDtCadastro() {
		return dtCadastro;
	}

	public void setDtCadastro(String dtCadastro) {
		this.dtCadastro = dtCadastro;
	}

	public Endereco getEndereco() {
		return endereco;
	}

	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}

	public Contato getContato() {
		return contato;
	}

	public void setContato(Contato contato) {
		this.contato = contato;
	}
	
	
	
	
	
}
