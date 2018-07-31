class Parks extends Component {
	constructor(props) {
		super(props);;
		this.state = {
      		error: null,
      		isLoaded: false,
      		items: []
    	};
    	this.origin = window.location.origin;
	}

	componentDidMount() {
		console.log("mounted");
	    fetch(this.origin + "/parks.json")
	      .then(res => res.json())
	      .then(
	        (result) => {
	        	console.log(result);
	          this.setState({
	            isLoaded: true,
	            items: result.items
	          });
	        },
	        // Note: it's important to handle errors here
	        // instead of a catch() block so that we don't swallow
	        // exceptions from actual bugs in components.
	        (error) => {
	          this.setState({
	            isLoaded: true,
	            error
	          });
	        }
	      )
	  }

  render() {
    return (
    	<div>Hello World</div>
    	);
    }
}
export default Parks;
