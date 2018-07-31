import React from 'react';
import {Link} from 'react-router-dom';
import Pagination from './pagination';
import {Thumbnail,Col,Button} from 'react-bootstrap';

export default class PageNotFound extends React.Component{   

render() {
    return (
        <div>
          <h1 style={{textAlign:'center'}} >Page Not Found</h1>
        </div>
    );
}
}